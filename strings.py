#EG, strings notes
name = input("What is your name: ").strip().capitalize()

age = input("How old are you: ")
print(type(age))

print(age + age)

print(name + " " + "LaRose")

sentence = "The quick brown fox jumps over the lazy dog"

print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name))

print(f"your name is {name} that is {len(name)} letters long. Your initial is {name[0]} I think i will call you {name[0:3]}")
