from pycoingecko import CoinGeckoAPI
import pandas as pd
cg = CoinGeckoAPI()

#a = cg.get_price(ids=['bitcoin', 'ethereum'], vs_currencies='eur')

#a = cg.get_coin_market_chart_range_by_id('bitcoin','eur',1642702654, 1643322882)

a = cg.get_coin_market_chart_by_id('bitcoin','eur',3196)

#print(((a['prices'][-1][1])/(a['prices'][0][1]))-1)

df = pd.Dataframe(a)
df.to_csv('bitcoin.csv')





