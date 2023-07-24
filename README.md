# PyCrypto
Python Library for working with Сryptocurrency using CoinGecko API

[![Documentation Status](https://readthedocs.org/projects/pycryptoo/badge/?version=latest)](https://pycryptoo.readthedocs.io/en/latest/?badge=latest)


Installing
----------

Install and update using [pip](https://pypi.org/project/pip/):

````
    pip install PyCrypto
````

Usage
-----

    
    
````
    Example using get_overview
    print(crypto.get_overview("bitcoin", "usd"))

    Example using get_price
    print(crypto.get_price("ethereum", "eur"))

    Example using get_market_cap
    print(crypto.get_market_cap("tether", "rub"))
````
    




Documentation
-------------

Documentation for this package can be found on [readthedocs](pycryptoo.readthedocs.io).



License
-------
MIT License

Copyright (c) 2023 limping

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
