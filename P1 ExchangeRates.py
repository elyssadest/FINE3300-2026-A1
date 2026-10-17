import pandas as pd #pandas is used to read the CSV file

class ExchangeRates: #Reads the Bank of Canada USD/CAD exchange rate file and converts between USD and CAD.
    def __init__(self): 
        df = pd.read_csv('BankofCanadaExchangeRate.2026.csv') #Load the CSV file into a table
        self.rate = df['FXAUSDCAD'].iloc[-1] #Take the last value in the column = latest rate

    def convert(self, amount, from_currency, to_currency): #Convert an amount between USD and CAD and return the converted amount
        if from_currency == "USD" and to_currency == "CAD": #Case 1: USD to CAD
            return amount * self.rate #Multiply by the rate
        elif from_currency == "CAD" and to_currency == "USD": #Case 2: CAD to USD
            return amount / self.rate #Divide by the rate
        else: #Any other case, same currency: no conversion needed
            return ("Invalid conversion. Please try again.") 

converter = ExchangeRates() #Create a converter object. This reads the CSV and stores the latest rate

amount = (float)(input("How much would you like to convert?: ")) #Ask for the amount and turn the text into a number

from_currency = input("From which currency? (USD or CAD) ").upper() #Ask for the starting currency, make it capitals
to_currency = input("To which currency? (USD or CAD) ").upper() #Ask for the target currency, make it capitals

output = converter.convert(amount, from_currency, to_currency) #Have the convert methond perform the math
print ("Success! You have completed the conversion from $", amount, from_currency, "to $", round (output, 2), to_currency) #Print the formatted result