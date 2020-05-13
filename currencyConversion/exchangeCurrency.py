import getCurrencyRates

def main():
    currencyList = getCurrencyRates.getCurrencyRates()
    print(currencyList)

if __name__ == '__main__':
    main()