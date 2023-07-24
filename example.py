from PyCrypto import crypto

# get_overview
# Example using get_overview
print(crypto.get_overview("bitcoin", "usd"))
# {'id': 'bitcoin', 'symbol': 'btc', 'name': 'Bitcoin', 'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579', 'current_price': 29135.0, 'market_cap': 566490100529, 'market_cap_rank': 1, 'fully_diluted_valuation': 612005660970.0, 'total_volume': 14724923368.0, 'high_24h': 30089.0, 'low_24h': 28983.0, 'price_change_24h': -939.7548818238247, 'price_change_percentage_24h': -3.12475, 'market_cap_change_24h': -19003325958.530396, 'market_cap_change_percentage_24h': -3.24569, 'circulating_supply': 19438206.0, 'total_supply': 21000000.0, 'max_supply': 21000000.0, 'ath': 69045.0, 'ath_change_percentage': -57.7928, 'ath_date': '2021-11-10T14:24:11.849Z', 'atl': 67.81, 'atl_change_percentage': 42876.39728, 'atl_date': '2013-07-06T00:00:00.000Z', 'roi': None, 'last_updated': '2023-07-24T21:19:49.525Z'}

# get_price
# Example using get_price
print(crypto.get_price("ethereum", "eur"))
# 1670.77

# get_market_cap
# Example using get_market_cap
print(crypto.get_market_cap("tether", "rub"))
# 7579879800255

