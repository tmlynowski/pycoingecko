"""COINGECKO EXAMPLES"""

#%% API Manual and original source code links
""" 
https://www.coingecko.com/api#
https://github.com/man-c/pycoingecko
"""

#%% IMPORTANT DISCLAIMER: www.coingecko.com 
"""
IMPORTANT DISCLAIMER: All content provided herein our website, hyperlinked sites, associated applications, forums, blogs, social media accounts
 and other platforms (“Site”) is for your general information only, procured from third party sources. We make no warranties of any kind in relation 
 to our content, including but not limited to accuracy and updatedness. No part of the content that we provide constitutes financial advice, legal 
 advice or any other form of advice meant for your specific reliance for any purpose. Any use or reliance on our content is solely at your own risk 
 and discretion. You should conduct your own research, review, analyse and verify our content before relying on them. Trading is a highly risky activity 
 that can lead to major losses, please therefore consult your financial advisor before making any decision. No content on our Site is meant to be a 
 solicitation or offer.

"""
#%%

#do library import
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
#%% Check API connection status

conn_status = cg.ping()
#%% List all supported coins id, name and symbol (no pagination required)

get_coins_list = cg.get_coins_list()
#%% Gets 50 top coin info

get_coins = cg.get_coins()
#%% List all supported coins price, market cap, volume, and market related data (no pagination required)

get_coin_markets=cg.get_coins_markets('USD',order = 'market_cap_desc') #sorted on market cap descending rank variosu sorts can be applied (see API manual)
#%% Get current data (name, price, market, ... including exchange tickers) for a coin

get_coin_by_id = cg.get_coin_by_id('bitcoin')
#%% Get historical data (name, price, market, stats) at a given date for a coin

get_coin_history = cg.get_coin_history_by_id('bitcoin', '30-12-2017')
#%% Get historical market data include price, market cap, and 24h volume (granularity auto)

get_market_chart = cg.get_coin_market_chart_by_id('bitcoin','USD','max') #note price data is in a list of date in an integer then , price. 
#%% List all exchanges
exchanges_list = cg.get_exchanges_list()
#%% Get exchange volume in BTC and top 100 tickers only

get_exchanges_by_id = cg.get_exchanges_by_id('bitfinex')
#%% Get cryptocurrency global data

get_global = cg.get_global()
#%%
