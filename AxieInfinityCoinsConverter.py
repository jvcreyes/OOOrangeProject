import json
import requests
class URL():
    def __init__(self, URL):
        self.URL = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
class GetCurrencyValue(URL):
    def __init__(self,from_currency, to_currency, api_key):
        URL.__init__(self,URL)
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
def main():
    while True:
        print("\n1 - Convert Official Currency"
              "\n2 - Convert SLP"
              "\n3 - Convert ETH"
              "\n4 - Convert AXS"
              "\n5 - Exit"
              "\nWhat would you like to do?:")
        user_input = int(input())
        if user_input == 1:
            from_currency = str(input("Convert: "))
            to_currency = str(input("To: "))
            api_key = "Q5GOJP1I9VYFSRPB"
            url = GetCurrencyValue(from_currency,to_currency,api_key)
            main_url = url.converge()
            GetData(main_url)
            Compute(main_url)
        if user_input == 5:
            exit()
main()