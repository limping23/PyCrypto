import enum

crypto_name = "bitcoin"
url = f"https://www.binance.com/en/price/{crypto_name}"


class Currency(enum.IntEnum):
    USD = 1
    GBP = 2
    EUR = 3
    CHF = 4
    RUB = 5
    PLN = 6
    BRL = 7
    JPY = 8
    NOK = 9
    IDR = 10
    MYR = 11
    PHP = 12
    SGD = 13
    THB = 14
    VND = 15
    KRW = 16
    TRY = 17
    UAH = 18
    MXN = 19
    CAD = 20
    AUD = 21
    NZD = 22
    CNY = 23
    INR = 24
    CLP = 25
    PEN = 26
    COP = 27
    ZAR = 28
    HKD = 29
    TWD = 30
    SAR = 31
    AED = 32
    ARS = 34
    ILS = 35
    # 36 is not supported
    KZT = 37
    KWD = 38
    QAR = 39
    CRC = 40
    UYU = 41


class Div(enum.Enum):
    price = "css-12ujz79"
    price_change = "css-12i542z"
    overview = "css-ru61a6"
    change = "css-3ep30v"
    today_min = "css-1ez451f"
    today_max = "css-1ez451f"
    all_max = "css-1o346il"
    volume = "css-1o346il"
    today_volume = "css-1o346il"
    capitalization = "css-1o346il"
    rate = "css-1o346il"
    crypto_trends = "css-1dkxekh"
    raise_liders = "css-1dkxekh"
    drop_liders = "css-1dkxekh"
    crypto_info = "richtext-container css-fbxu07"
    crypto_website = "css-y3rmjb"
