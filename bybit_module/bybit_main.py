from configparser import ConfigParser
from bybit_module._v5_market import MarketHTTP

def make_orderbook_bybit():
    config = ConfigParser()
    config.read('config.ini')
    data = config["data"]
    key = data['key']
    secret = data['secret']
    session2 = MarketHTTP(api_key=key, api_secret=secret, testnet=False)
    #r = session2.get_orderbook(category="linear", symbol="BTCUSDT")
    return session2.get_orderbook(category="linear", symbol="BTCUSDT")
