# • Modify the program so that the user can see the equivalent amount in several 
# different currencies at the same time. For example, converting 100 USD to 
# EUR, CAD, and GBP all at once. 
# • Expand the list of available currencies for conversion. This might involve 
# adding more fixed exchange rates to the program. 
# • Keep a history of the most recent conversions made during the session and 
# display this history at the end of the program. 

import os

currencies = {
    "USD": "United States Dollar",
    "EUR": "Euro",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "CHF": "Swiss Franc",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "NZD": "New Zealand Dollar",
    "CNY": "Chinese Yuan",
    "INR": "Indian Rupee",
    "ZAR": "South African Rand",
    "RUB": "Russian Ruble",
    "BRL": "Brazilian Real",
    "MXN": "Mexican Peso",
    "SGD": "Singapore Dollar",
    "HKD": "Hong Kong Dollar",
    "SEK": "Swedish Krona",
    "NOK": "Norwegian Krone",
    "KRW": "South Korean Won",
    "TRY": "Turkish Lira",
    "PKR": "Pakistani Rupee"
}

rates = {
    "USD": 1.00,
    "EUR": 0.93,
    "GBP": 0.77,
    "JPY": 152.59,
    "CHF": 0.87,
    "CAD": 1.39,
    "AUD": 1.50,
    "NZD": 1.66,
    "CNY": 7.16,
    "INR": 84.37,
    "ZAR": 17.45,
    "RUB": 97.85,
    "BRL": 5.69,
    "MXN": 19.77,
    "SGD": 1.32,
    "HKD": 7.77,
    "SEK": 10.73,
    "NOK": 10.91,
    "KRW": 1385.56,
    "TRY": 34.36,
    "PKR": 277.60,
}

while True:
    try:
        SourceAmount = int(input("Enter the Amount(Number): "))
    except ValueError:
        print("I said a Bloody Number.")
        continue
    if SourceAmount < 1: print("I said an amount not bloody zero.")
    else: break

os.system("cls")
while True:
    for i, (code, name) in enumerate(currencies.items(), start=1):
        print(f"{i}. {code}: {name}")
    SourceCurrency = input("Enter The Currency Of The Amount:").strip().upper()
    if SourceCurrency not in currencies: print("Enter a Currency which is in the list of currencies available.")
    else: break

os.system("cls")

print(f"Your Amount with Currency: {SourceAmount} {SourceCurrency}. ")

def CurrencyConverter(SOURCE_AMMOUNT, SOURCE_CURRENCY, TARGET_CURRENCY):
        # Correct conversion formula
    converted_amount = SOURCE_AMMOUNT * (rates[TARGET_CURRENCY] / rates[SOURCE_CURRENCY])
    print(f"{SOURCE_AMMOUNT} {SOURCE_CURRENCY} is equal to {converted_amount} {TARGET_CURRENCY}.")
        
def AllCurrencyConverter(SOURCE_AMOUNT,SOURCE_CURRENCY):
    for keys,value in rates.items():
        converted_amount = SOURCE_AMOUNT * (value/rates[SOURCE_CURRENCY])
        print(f"{SOURCE_AMOUNT} {SOURCE_CURRENCY} is equal to {converted_amount} {keys}.")

def SingleCurrencyConversion():
    while True:
        for i, (code, name) in enumerate(currencies.items(), start=1):
            print(f"{i}. {code}: {name}")
        TargetCurrency = input("Which currency to convert?: ").strip().upper()
        if TargetCurrency not in currencies: print("Enter a Currency which is in the list of currencies available.")
        else: break

    os.system("cls")

    print(f"Your Amount With Currency: {SourceAmount} {SourceCurrency}. ")
    print(f"Your Converting Amount With Currency: {TargetCurrency} - {currencies[TargetCurrency]}")
    CurrencyConverter(SourceAmount,SourceCurrency,TargetCurrency)
    
def MultiCurrencyConversion():
    print(f"Your Amount With Currency: {SourceAmount} {SourceCurrency}. ")
    AllCurrencyConverter(SourceAmount,SourceCurrency)

while True:
    single_or_multi_currency_conversion = input("Do you want to do single conversion or multi-conversion? (single/s/multi/m) \n: ").strip().lower()
    if single_or_multi_currency_conversion == "single" or single_or_multi_currency_conversion == "s":
        SingleCurrencyConversion()
        break
    elif single_or_multi_currency_conversion == "multi" or single_or_multi_currency_conversion == "m":
        MultiCurrencyConversion()
        break
    else: print("Enter 'multi' or 'm' or 's' or 'single' ")
    

with open("History Of Currency Exchanges.txt","w") as writer:
    pass