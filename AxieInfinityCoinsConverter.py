import json
import requests

class URL():

    def __init__(self, URL):
        self.URL = URL
        self.URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"


class GetCurrencyValue(URL):

    def __init__(self,from_currency, to_currency, api_key):
        URL.__init__(self, URL)
        self.URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.api_key = api_key

    def converge(self):
        self.converge = self.URL + "&from_currency=" + self.from_currency + "&to_currency=" + self.to_currency + "&apikey=" + self.api_key
        main_url = self.converge
        return main_url


def GetData(main_url):
    URLdata = requests.get(main_url)
    URLdatajson = URLdata.json()
    print("1",URLdatajson["Realtime Currency Exchange Rate"]["2. From_Currency Name"], "=", URLdatajson["Realtime Currency Exchange Rate"]
          ['5. Exchange Rate'],URLdatajson["Realtime Currency Exchange Rate"]["4. To_Currency Name"])
    x = URLdatajson["Realtime Currency Exchange Rate"]['5. Exchange Rate']
    return x


def Compute(main_url):
    URLdata = requests.get(main_url)
    URLdatajson = URLdata.json()
    x_raw = URLdatajson["Realtime Currency Exchange Rate"]['5. Exchange Rate']
    x = round(float(x_raw),4)
    value = round(float((input("Enter Amount In "+URLdatajson["Realtime Currency Exchange Rate"]["2. From_Currency Name"]+":"))))
    result = (value)*(x)
    print(value,URLdatajson["Realtime Currency Exchange Rate"]["2. From_Currency Name"],"=",result,URLdatajson["Realtime Currency Exchange Rate"]["4. To_Currency Name"])


class CGURL():
    def __init__(self, CGURL):
        self.CGURL = "https://api.coingecko.com/api/v3/simple/price?"


class GetCurrencyValueSLP(CGURL):

    def __init__(self, vs_currencies):
        CGURL.__init__(self,CGURL)
        self.CGURL = "https://api.coingecko.com/api/v3/simple/price?"
        self.vs_currencies = vs_currencies

    def convergeSLP(self):
        self.converge = self.CGURL + "ids=smooth-love-potion&vs_currencies=" + self.vs_currencies
        main_urlSLP = self.converge
        return main_urlSLP


class GetCurrencyValueETH(CGURL):

    def __init__(self, vs_currencies):
        CGURL.__init__(self, CGURL)
        self.CGURL = "https://api.coingecko.com/api/v3/simple/price?"
        self.vs_currencies = vs_currencies

    def convergeETH(self):
        self.convergeETH = self.CGURL + "ids=ethereum&vs_currencies=" + self.vs_currencies
        main_urlETH = self.convergeETH
        return main_urlETH


class GetCurrencyValueAXS(CGURL):

    def __init__(self, vs_currencies):
        CGURL.__init__(self, CGURL)
        self.CGURL = "https://api.coingecko.com/api/v3/simple/price?"
        self.vs_currencies = vs_currencies

    def convergeAXS(self):
        self.convergeAXS = self.CGURL + "ids=axie-infinity&vs_currencies=" + self.vs_currencies
        main_urlAXS = self.convergeAXS
        return main_urlAXS


def GetDataSLP(main_url, vs_currencies):
    URLdataSLP = requests.get(main_url)
    URLdataSLPjson = URLdataSLP.json()
    print("Realtime Currency Exchange Rate for 1 Smooth Love Potion (SLP) is",
          URLdataSLPjson["smooth-love-potion"]
          [vs_currencies], vs_currencies)
    x = URLdataSLPjson["smooth-love-potion"][vs_currencies]
    return x


def GetDataETH(main_url, vs_currencies):
    URLdata = requests.get(main_url)
    URLdatajson = URLdata.json()
    print("Realtime Currency Exchange Rate for 1 Ethereum (ETH) is",
          URLdatajson["ethereum"]
          [vs_currencies], vs_currencies)
    x = URLdatajson["ethereum"][vs_currencies]
    return x


def GetDataAXS(main_url, vs_currencies):
    URLdata = requests.get(main_url)
    URLdatajson = URLdata.json()
    print("Realtime Currency Exchange Rate for 1 Axie Infinity (AXS) is",
          URLdatajson["axie-infinity"]
          [vs_currencies], vs_currencies)
    x = URLdatajson["axie-infinity"][vs_currencies]
    return x


def ComputeSLP(main_url, vs_currencies):
    URLdataSLP = requests.get(main_url)
    URLdataSLPjson = URLdataSLP.json()
    x_raw = URLdataSLPjson["smooth-love-potion"][vs_currencies]
    x = round(float(x_raw), 4)
    value = round(float(
        (input("Enter Amount In Smooth Love Potion (SLP): "))))
    result = (value) * (x)
    print(value,"SLP", "=", result, vs_currencies)


def ComputeETH(main_url, vs_currencies):
    URLdata = requests.get(main_url)
    URLdatajson = URLdata.json()
    x_raw = URLdatajson["ethereum"][vs_currencies]
    x = round(float(x_raw), 4)
    value =float((input("Enter Amount In Ethereum (ETH): ")))
    result = (value) * (x)
    print(value,"ETH", "=", result, vs_currencies)


def ComputeAXS(main_url, vs_currencies):
    URLdata = requests.get(main_url)
    URLdatajson = URLdata.json()
    x_raw = URLdatajson["axie-infinity"][vs_currencies]
    x = round(float(x_raw), 4)
    value = round(float((input("Enter Amount In Axie Infinity (AXS): "))))
    result = (value) * (x)
    print(value,"AXS", "=", result, vs_currencies)


def main():
    while True:
        print("\n1 - Convert Fiat Currency"
              "\n2 - Convert SLP"
              "\n3 - Convert ETH"
              "\n4 - Convert AXS"
              "\n5 - Exit"
              "\nWhat would you like to do?:")
        user_input = int(input())

        if user_input == 1:
            from_currency = str(input("Convert from: "))
            to_currency = str(input("To: "))
            api_key = "Q5GOJP1I9VYFSRPB"
            url = GetCurrencyValue(from_currency,to_currency,api_key)
            main_url = url.converge()
            GetData(main_url)
            Compute(main_url)

        if user_input == 2:
            vs_currencies = str(input("Convert SLP to: "))
            url = GetCurrencyValueSLP(vs_currencies)
            main_url = url.convergeSLP()
            GetDataSLP(main_url, vs_currencies)
            ComputeSLP(main_url, vs_currencies)

        if user_input == 3:
            vs_currencies = str(input("Convert ETH to: "))
            url = GetCurrencyValueETH(vs_currencies)
            main_url = url.convergeETH()
            GetDataETH(main_url, vs_currencies)
            ComputeETH(main_url, vs_currencies)

        if user_input == 4:
            vs_currencies = str(input("Convert AXS to: "))
            url = GetCurrencyValueAXS(vs_currencies)
            main_url = url.convergeAXS()
            GetDataAXS(main_url, vs_currencies)
            ComputeAXS(main_url, vs_currencies)

        if user_input == 5:
            print("~Thank you for using Axie Infinity Coins Converter!~")
            exit()
            
main()