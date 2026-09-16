#EG, Integers, Floats and expression notes

#Interger => whole numbers
students = 23
cars = 50
computers = 29
awareness = -12

# Float = Numbers with decimals
pi = 3.14
temp = -95.6
cost = 1.99
rain = 2.17

#rithmetic operators (+ - * / // ** %)
print(f"18/4 is {18/4} or {18//4} with a remainder of {18%4}")
print(f"18/5 is {18/5} or {18//5} with a remainder of {18%5}")

# order of operations
grades = (85+66+94+72)
students = len(grades)
avarage = sum(grades)/students
print(f"the avarage is {int (avarage)}")

# convert the data type
price = float (input("How much much did the item cost: "))
tax = 0.0485
sales_tax = price * tax
total = price + sales_tax
print(f"your total is {total}")
