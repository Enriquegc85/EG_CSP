#EG, loop starter

for num in range(1, 21):
    if num % 15 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)

count = 2 
while count <= 20:
    print(count)
    count += 2

for num in range(2, 21, 2):
    print(num)

siblings = ["Marisol" , "Maribel" , "Fernando"]
count = 1 
if len(siblings) > 0:
    while count <= len(siblings):
        print(f"{count}. {siblings[count - 1]}")
        count += 1
else:
    print("No siblings found.")