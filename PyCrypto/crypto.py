from PyCrypto import request

"""
USD SETS ON DEFAULT
LIST OF ALL SUPPORTED CRYPTOCURRENCIES IS AT 'all_supported_cryptocurrencies.txt'
"""


def get_overview(crypto_name: str, currency="usd") -> dict | None:
    """
           Gets the brief description of a coin.

           :param crypto_name: The name of the coin how it appears on CoinGecko.
           :type crypto_name: :class:`str`
           :param currency: The name of the currency (e.g. "eur"), "usd" sets on default
           :type currency: :class:`str`
           :return: An overview of the item on success, :class:`None` otherwise. Overview includes brief description of an item.
           :rtype: Optional[:class:`dict`]

           .. versionadded:: 1.0.0
           """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    overview = request(crypto_name, currency)
    if overview:
        return overview
    else:
        return None


def get_price(crypto_name: str, currency="usd", show_time=False) -> float | str | None:
    """
           Gets the price of a coin.

           :param show_time: OPTIONAL, False on default, shows the time, when price was updated (UTC+0)
           :type show_time: bool
           :param crypto_name: The name of the coin how it appears on CoinGecko.
           :type crypto_name: :class:`str`
           :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
           :type currency: :class:`str`
           :return: Price of the item on success, :class:`None` otherwise.
           :rtype: Optional[:class:`float`], if show_time=True: [:class:`str`]

           .. versionadded:: 1.0.0
           """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")
    if not isinstance(show_time, bool):
        raise TypeError(f"param show_time must be str not {type(crypto_name)}")

    coin_data = get_overview(crypto_name, currency)

    if show_time:
        return f'{coin_data["current_price"]}\n{coin_data["last_updated"].replace("T", " ").replace("Z", " ")}'
    else:
        return coin_data["current_price"]


def get_market_cap(crypto_name: str, currency="usd") -> int | None:
    """
            Gets the market capitalization of a coin.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: Market capitalization of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`int`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["market_cap"]


def get_market_cap_rank(crypto_name: str, currency="usd") -> int | None:
    """
            Gets the market capitalization rank in the world of a coin.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: Market capitalization rank of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`int`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["market_cap_rank"]


def get_fully_diluted_valuation(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the Fully Diluted Value (FDV) of a coin.

            Fully diluted valuation (FDV) is the total value of a cryptocurrency project assuming all of its tokens are
            in circulation.
            FDV is obtained by multiplying the current market price of a crypto asset by its maximum supply.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: Fully Diluted Value (FDV) of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["fully_diluted_valuation"]


def get_total_volume(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the total volume (24H) of a coin.

            The cryptocurrency volume refers to the total number of tokens or coins traded in a given period (24H).

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: Total volume of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["total_volume"]


def get_high_24h(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the highest price (24H) of a coin.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The highest price of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["high_24h"]


def get_low_24h(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the lowest price (24H) of a coin.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The lowest price of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["low_24h"]


def get_price_change_24h(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the price change (24H) of a coin.

            Price change (24H) is the difference between the lowest price of a coin and the highest price in 24 hours.

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The price change of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["price_change_24h"]


def get_market_cap_change_24h(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the market capitalization change (24H) of a coin.

            Market capitalization change (24H) is the difference between the lowest capitalization of a coin and the highest in 24 hours.

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The market capitalization change of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["market_cap_change_24h"]


def get_circulating_supply(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the Circulating Supply of a coin.

            The term circulating supply refers to the number of cryptocurrency coins or tokens that are publicly available and circulating in the market.

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The Circulating Supply of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["circulating_supply"]


def get_total_supply(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the Total Supply of a coin.

            Total supply refers to the number of coins or tokens that currently exists and are either in circulation or locked somehow.

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The Circulating Supply of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["total_supply"]


def get_ath(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the ATH of a coin.

            The term “All-Time High” relates to the highest price that an asset has achieved on an exchange, for the current trading pair that is being referenced.

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The lowest price of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["ath"]


def get_ath_change_percentage(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the difference between current price of a coin and ATH and shows it in percents.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The difference of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["ath_change_percentage"]


def get_ath_date(crypto_name: str, currency="usd") -> str | None:
    """
            Gets the date of ATH of a coin.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The date of ATH price of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`str`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["ath_date"]


def get_atl(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the ATL of a coin.

            The term “All-Time Low” relates to the lowest price that an asset has achieved on an exchange, for the current trading pair that is being referenced.

            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The ATL price of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["atl"]


def get_atl_change_percentage(crypto_name: str, currency="usd") -> float | None:
    """
            Gets the difference between current price of a coin and ATL and shows it in percents.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The difference of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`float`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["atl_change_percentage"]


def get_atl_date(crypto_name: str, currency="usd") -> str | None:
    """
            Gets the date of ATL of a coin.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :param currency: The name of the currency (e.g. "usd"), "usd" sets on default
            :type currency: :class:`str`
            :return: The date of ATL of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`str`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")
    if not isinstance(currency, str):
        raise TypeError(f"currency must be str not {type(currency)}")

    coin_data = get_overview(crypto_name, currency)

    return coin_data["atl_date"]


def get_crypto_link(crypto_name: str) -> str | None:
    """
            Gets the URL of the given cryptocurrency on CoinGecko.


            :param crypto_name: The name of the coin how it appears on CoinGecko.
            :type crypto_name: :class:`str`
            :return: The URL of the item on success, :class:`None` otherwise.
            :rtype: Optional[:class:`str`]

            .. versionadded:: 1.0.0
            """
    if not isinstance(crypto_name, str):
        raise TypeError(f"name must be str not {type(crypto_name)}")

    return f"https://www.coingecko.com/en/coins/{crypto_name}"





