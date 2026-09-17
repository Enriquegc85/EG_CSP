#EG, Your budget yay
monthly_income = float(input("What is your monthly income?"))
monthly_rent = float(input("What is your monthly rent?"))
monthly_utilities = float(input("what is your monthly utilitie bill?"))
monthly_groceries = float(input("what is your monthly groceries bill?"))
monthly_transportation = float(input("what is your monthly transportation bill? "))

rent_1 = int(round((monthly_rent / monthly_income) * 100))
utilities_1 = int(round((monthly_utilities / monthly_income) * 100))
grocerie_1 = int(round((monthly_groceries / monthly_income) * 100))
transportation_1 = int(round((monthly_transportation / monthly_income) * 100))

saving = monthly_income * 0.10
savings = 10

spending_money = monthly_income - monthly_rent - monthly_utilities - monthly_groceries - monthly_transportation - saving

print(f"Your monthly rent is ${monthly_rent} and that is {rent_1}% of your income")
print(f"Your monthly utilities bill is ${monthly_utilities} and that is {utilities_1}% of your income")
print(f"Your monthly groceries bill is ${monthly_groceries} and that is {grocerie_1}% of your income")
print(f"Your monthly transportation bill is ${monthly_transportation} and that is {transportation_1}% of your income")
print(f"Your monthly savings is ${saving} and that is {savings}% of your income")
print(f"Your monthly spending money is ${spending_money}")