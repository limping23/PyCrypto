from pycoingecko import CoinGeckoAPI
import pandas as pd


def request(coin_name, currency="usd"):
    cg = CoinGeckoAPI()
    try:
        all_coins_market = cg.get_coins_markets(vs_currency=currency.lower())
        all_coins_market_df = pd.DataFrame(all_coins_market)
        filtered_df = all_coins_market_df[all_coins_market_df['id'] == coin_name]
        coin_data = filtered_df.iloc[0].to_dict()
        return coin_data
    except ValueError:
        return TypeError(f"Invalid name of the currency '{currency}', or currency is not supported")
    except IndexError:
        return TypeError(f"Invalid name of the cryptocurrency '{coin_name}', or cryptocurrency is not supported yet")

