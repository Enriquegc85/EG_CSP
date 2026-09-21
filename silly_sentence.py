#EG, Silly sentences
while True:
    verb = input("Tell me a verb ending in ing: ").strip().lower()
    if verb.isnumeric():
        print("Please enter a valid verb.")
    elif not verb.endswith("ing"):
        print("Please enter a verb that ends with 'ing'.")
    else:
        break
while True:
    place = input("Tell me a place: ").strip().lower()
    if place.isnumeric():
        print("Please enter a valid place.")
    else:
        break
while True:
    color = input("Tell me a color: ").strip().lower()
    if color.isnumeric():
        print("Please enter a valid color.")
    else:
        break
while True:
    travel_way = input("Tell me a way to travel: ").strip().lower()
    if travel_way.isnumeric():
        print("Please enter a valid way to travel.")
    else:
        break
while True:
    emotion = input("Tell me an emotion: ").strip().lower()
    if emotion.isnumeric():
        print("Please enter a valid emotion.")
    else:
        break
while True:
    animal = input("Tell me an animal: ").strip().lower()
    if animal.isnumeric():
        print("Please enter a valid animal.")
    else:
        break

print("It was a " + color + " day in " + place + ". I was " + verb + " to school when I saw a " + animal + " that made me feel very " + emotion + ". I decided to take a break and travel by " + travel_way + ".")