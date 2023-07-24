.. PyCrypto documentation master file, created by
   sphinx-quickstart on Tue Jul 11 11:14:09 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyCrypto
====================================
get_overview()
           Gets the brief description of a coin.

           :param crypto_name: The name of the coin how it appears on CoinGecko.
           :type crypto_name: :class:`str`
           :param currency: The name of the currency (e.g. "eur"), "usd" sets on default
           :type currency: :class:`str`
           :return: An overview of the item on success, :class:`None` otherwise. Overview includes brief description of an item.
           :rtype: Optional[:class:`dict`]

           .. versionadded:: 1.0.0
         




