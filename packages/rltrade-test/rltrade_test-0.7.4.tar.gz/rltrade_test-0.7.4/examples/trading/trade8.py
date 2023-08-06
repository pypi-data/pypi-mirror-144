import asyncio
from metaapi_cloud_sdk import MetaApi
from rltrade import config
from rltrade.backtests import get_metrics
from rltrade.models import SmartTradeAgent

#USDCAD/USDCHF - 3 epochs
#EURUSD/GBPUSD - 2 epochs
#AUDUSD/NZDUSD - 2 epochs

demo=True
time_frame = "1d" #keep is 1d in this file or else it won't work
trade_period = ('2021-12-20','2021-12-28') #(last test date, yesterday's date)
start_time_str = "17:00:00"
end_time_str = "23:59:00"
path = 'models/dailytrade/forex-CADCHF'

token = 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiIzYTI0YzMwYzFkNDRmZGFmZGI3NmVmYTUxZmQ2MDJmMCIsInBlcm1pc3Npb25zIjpbXSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaWF0IjoxNjM5NDkwMzEzLCJyZWFsVXNlcklkIjoiM2EyNGMzMGMxZDQ0ZmRhZmRiNzZlZmE1MWZkNjAyZjAifQ.DhA6Q-AlWNssi8ScOaWy2Bxo4Hebgw94BDE6PiT9J-TvsuF7OqvdYBQ1IWYEMtsYsg3Ij8p8Wpvn8ZdZeHRkR3vLcQnMH-GZj3DyYkeqovQKk6U3uOobV-GS3meJPZYfw2zItuTDBWxuHDZsVW1ZvF4sItBDmsWIe2svF0NmKE1nu-ephcYVzYo9grr93de_h-QwlP-yeZFeGEqrz3-q5gYWcARJsIR1BX63zePuDHkUK9k5W9Rm28WdB87MHEyMSWhcAZDf8si5MwsPYC3wpzNtzGqORF3UY-w5EmolCtSPMBqM7AI0LKc1n8GPS3ZhnvHkfGhWEdb5gKlCWwshk30tICN24C1bZG06zfs450oLm8ih9ls5oyshcg_xwawNvsA305D7Siz0Pzqr1xnUA8zMz8cVUFZtjdBWCfot05_ziVO0x_mApVyAVC2OA-Sh61RtkwNNpg4bTCzK30OpdiS9GO0HLgnepnuwWOO0T9DTzTAJUxyJcXOzcWcXGdMTWaGAp5ranytU97k8GxDHa5jOS_WvphL24C8QA6of0pYZwHM3Ul5Aw351H1SbJLIqs2AChDoUnpJb9OZb-27ESLZgM1mhU6rwzt8lRRbxUHaXSv5QpM29nPm3k5KrFSv-UTXiX6oU9c1nNh3qLb6FKV_B1CQarcvyx66iUg-1DcU'
domain = 'agiliumtrade.agiliumtrade.ai'

if demo:
    account_id = '9d20d731-3188-42de-9db9-e586675bff23'
else:
    account_id = 'ddc8fb93-e0f5-4ce8-b5d5-8290d23fc143'

tech_indicators = config.STOCK_INDICATORS_LIST # indicators from stockstats
additional_indicators = config.ADDITIONAL_STOCK_INDICATORS

env_kwargs = {
    "initial_amount": 17500, #this does not matter as we are making decision for lots and not money.
    "ticker_col_name":"tic",
    "stop_loss":0.015,
    "filter_threshold":1, #between 0.1 to 1, select percentage of top stocks 0.3 means 30% of top stocks
    "target_metrics":['asset'], #asset, cagr, sortino, calamar, skew and kurtosis are available options.
    "transaction_cost":0, #transaction cost per order
    "tech_indicator_list":tech_indicators + additional_indicators, 
    "reward_scaling": 1}

A2C_PARAMS = {"ent_coef": 0.01, 
            "learning_rate": 0.0001}


async def run_main():
    api = MetaApi(token,{'domain':domain})
    try:
        #connecting it once
        account = await api.metatrader_account_api.get_account(account_id)
    
        if account.state != 'DEPLOYED':
            print("Deploying account")
            await account.deploy()
        else:
            print('Account already deployed')
        if account.connection_status != 'CONNECTED':
            print('Waiting for API server to connect to broker (may take couple of minutes)')
            await account.wait_connected()
        else:
            print('Account already connected')
        
        agent = SmartTradeAgent("a2c",
                            df=None,
                            ticker_list=None,
                            sec_types=None,
                            exchanges=None,
                            train_period=None,
                            test_period=None,
                            account=account,
                            time_frame=time_frame,
                            ticker_col_name="tic",
                            tech_indicators=tech_indicators,
                            additional_indicators=additional_indicators,
                            start_time=start_time_str,
                            end_time=end_time_str,
                            env_kwargs=env_kwargs,
                            model_kwargs=A2C_PARAMS,
                            tb_log_name='a2c',
                            epochs=3)


        agent.load_model(path) #same path as save
        actions = await agent.get_trade_actions(trade_period)

        streaming_connection = account.get_streaming_connection()
        print('Streaming connection...')
        await streaming_connection.connect()
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await streaming_connection.wait_synchronized()

        await agent.make_trade(actions,account,streaming_connection)

        print("-----------------------------------------")
        
    except Exception as err:
            print(api.format_error(err))
    
    exit()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(run_main())
get_metrics(path,live=True)