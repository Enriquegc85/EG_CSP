#EG, functions

def stupid_proof(money):
    while True:
        try:
            amount = float(input(f"what is your monthly {money}: "))
            return amount
        except:
            print("that isnt a number >:/")

# frist thing you should do is write all your variables
income = stupid_proof("income")
rent = stupid_proof("rent")
utilities = stupid_proof("utilities")
groceries = stupid_proof("groceries")
transportation = stupid_proof(transportation)

savings = income * 0.10


#second thing you should do is writter all ur functions
def calc_percentage(bill, income):
    return round(bill / income * 100)


#third is any outputs to your user
print(f"Your rent is ${rent:.2f} which is {calc_percentage(rent, income)}% of your income")
print(f"Your utilities is ${utilities:.2f} which is {calc_percentage(utilities, income)}% of your income")
print(f"Your groceries is ${groceries:.2f} which is {calc_percentage(groceries, income)}% of your income")
print(f"Your transportation is ${transportation:.2f} which is {calc_percentage(transportation, income)}% of your income")
print(f"Your savings is ${savings:.2f} which is {calc_percentage(savings, income)}% of your income")
print(f"you have to save ${savings:.2f} per month to reach your goal of saving 10% of your income")
print(f"you have ${income - rent - utilities - groceries - transportation - savings:.2f} left over to spend.")
