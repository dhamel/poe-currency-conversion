import getCurrencyRates
import sys

def convert(source,target,amount,currencyList):
    #takes in the source currency, the currency you want to convert to, 
    # the amount of the currency you want to convert to, and the currency information list
    sourceCurr =  None
    targetCurr = None
    for i in currencyList:
        if i.name == source:
            sourceCurr = i
            break
    for i in currencyList:
        if i.name == target:
            targetCurr = i
            break

    targetChaosEquiv = targetCurr.value * float(amount)
    return sourceCurr.value * targetChaosEquiv

def main():
    currencyList = getCurrencyRates.getCurrencyRates()
    #print(currencyList)
    if len(sys.argv) > 1:
        amount = sys.argv[2]
        target = sys.argv[3]
        source = sys.argv[1]

        print(str(amount) + " of " + target + " is equivilant to " + str(convert(source,target,amount,currencyList))+ " " + source)

if __name__ == '__main__':
    main()