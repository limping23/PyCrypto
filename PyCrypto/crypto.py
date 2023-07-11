from request import request
from enums import Currency, Div



class Crypto:

    def __init__(self, currency=Currency.USD):
        """Sets the currency to be outputted.

        :param currency: Currency used for prices.
        :type currency: :class:`Currency`, :class:`int`, :class:`str`
        """

        if isinstance(currency, Currency):
            self.currency = currency.value

        elif isinstance(currency, str):
            self.currency = Currency[currency.upper()].value

        elif isinstance(currency, int):
            self.currency = Currency(currency).value

        else:
            self.currency = 1

    def get_crypto_overview(self, crypto_name: str):
        """
                Gets the prices and volume of a currency.

                :param crypto_name: The name of the currency how it appears on Binance.
                :type crypto_name: :class:`str`
                :return: An overview of the item on success, :class:`None` otherwise. Overview includes both volume and prices.
                :rtype: Optional[:class:`str`]
        """
        if not isinstance(crypto_name, str):
            raise TypeError(f"name must be str not {type(crypto_name)}")

        overview = request(div=Div.overview)
        return overview


cr = Crypto()
cr.get_crypto_overview("bitcoin")






