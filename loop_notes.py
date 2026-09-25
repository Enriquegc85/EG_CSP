#EG, loop notes
import random


count = 1
while count <= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)
while True:
    if ducks == goose:
        break
    print("Duck. . . .")
    ducks += 1 #ducks = ducks + 1
print("GOOSE!!!!")

# complex data type holds other data types, like strings, integers, floats, and even other lists
siblings = ["Marisol" , "Maribel" , "Fernando"]
print(siblings[0])
siblings.append("Enrique") #this adds things to the end of the list
print(siblings)
siblings.insert(3, "Enrique")
print(siblings)
# to rmeove and item from a list
siblings.pop(3) #if no number given pop removces last item on the list item

#print each item in a list 
for sibling in sibling:
     print(sibling)
#adding to lists
#for loops

for num in range(1,25):
    print(num)
    if num %15 == 0:
        print("fizzbuzz")
    elif num %3 == 0:
            print("fizz")
    elif num %5 == 0:
            print("buzz")
    else:
        print(num)