print("Hi! I'm a currency conversion calculator! ")

def euros(dollars):
    dollars = float(dollars)
    return dollars * 0.84

def yen(dollars):
    dollars = float(dollars)
    return dollars * 109.83

def pounds(dollars):
    dollars = float(dollars)
    return dollars * 0.73

def pesos(dollars):
    dollars = float(dollars)
    return dollars * 19.97

def run_calculator(currency, dollars):
    possible_currencies = ["euros", "yen", "pounds", "pesos"]
    if currency not in possible_currencies:
        print("Invalid currency")
    else:
        if currency == "euros":
            print(str(euros(dollars)) + " euros")
        elif currency == "yen":
            print(str(yen(dollars)) + " yen")
        elif currency == "pounds":
            print(str(pounds(dollars)) + " pounds")
        elif currency == "pesos":
            print(str(pesos(dollars)) + " pesos")

    
    
currency = input("Would you like to convert from dollars to euros, yen, pounds or pesos?: ")
dollars = input("Your dollar amount: ")
run_calculator(currency, dollars)
