#! python3

import requests,json

class Currency:
     def __init__(self,name,value):
          self.name = name
          self.value = value
     def __repr__(self):
          return self.name + " : " + str(self.value)

def getCurrencyRates():
     response = requests.get("https://poe.ninja/api/data/currencyoverview?league=Delirium&type=Currency")
     data = response.json().get("lines")

     currencyList = []

     for i in data:
          currencyList.append(Currency(i.get("currencyTypeName"),i.get("chaosEquivalent")))

     currencyList.append(Currency("Chaos Orb",1))
     print(currencyList)
     return currencyList

