#EG, Conditionals notes yay

#conditional

time = 1416
day = "tuesday"

if time < 1200 and time > 500:
    print("Good morning")
elif time < 1700:
    if day != "saturday" and day != "sunday":
        print("Good afternoon")
elif time < 2000:
    print("Good evening")
else:
    print("Good night!")


print("Code is done")