from okx_module.MarketData import MarketAPI
from collections import defaultdict

"""
import okx.MarketData as MarketData
marketDataAPI = MarketData.MarketAPI(flag=flag)
print(starting_time)

result = marketDataAPI.get_tickers(instType="SPOT"
)
pprint(result)

result = marketDataAPI.get_ticker(instId='BTC-USDT')
pprint(result)
def short_dfs(root, depth, profit):
    if depth >= 5:
        return
    else:
        depth += 1
        short_dfs(root, depth, profit)
0"""


def make_tickers_okx():
    graph = defaultdict(dict)
    flag = "0"  # live trading: 0, demo trading: 1
    marketDataAPI = MarketAPI(flag=flag)
    res = marketDataAPI.get_tickers(instType="SPOT")['data']
    for row in res:
        askPx = row['askPx']
        bidPx = row['bidPx']
        from_coin, to_coin = row['instId'].split('-')  # row['instId'] = instId
        graph[from_coin][to_coin] = max(askPx, bidPx)
    return graph



import pprint

graph = make_tickers_okx()
pprint.pprint(graph)
"""
for key, val in graph.items():
    root_usdt = graph['USDT'][key]
    if root_usdt is not None:
        short_dfs(root_usdt, 0, 0)"""

