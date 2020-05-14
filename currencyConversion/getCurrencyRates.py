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
     return currencyList
#print(currencyList)

#TODO
#maybe put this in its own file and make the getting currency its own function?
#take 3 use command line inputs: starting currency type (currency i have, end currency type, and the amount of the end currency)
#example: the item i want to buy costs 1.4 ex, but i only have fusings, how many fusings is 1.4 ex?
#continue reading on how to structure a python project
