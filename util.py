from polygon import RESTClient as plygRESTC
from typing import cast
from urllib3 import HTTPResponse
import json
from configparser import ConfigParser
import pandas as pd

config_object = ConfigParser()
config_object.read("config/config.ini")
DEBUG_PRINT = config_object['main']['DEBUG_PRINT']

# Grab TD configuration values.
polygon_api_key = config_object.get('main', 'POLYGON_API_KEY')
polygon_client = plygRESTC(polygon_api_key)
POLYGON_TRADES_HISTORY_RESPONSE_LIMIT = 50000

def get_ticker_list():

    tickers = cast(
        HTTPResponse,
        polygon_client.get_snapshot_all(market_type='stocks', include_otc=True, raw=True),
    )


    ddict = json.loads(tickers.data.decode("utf-8"))
    tickers_df = pd.DataFrame(ddict['tickers'])

    return tickers_df['ticker'].sort_values().tolist()

tickers = get_ticker_list()
pass
