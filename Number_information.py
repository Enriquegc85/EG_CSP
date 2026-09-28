#EG, Number information
for num in range(1, 21):
    if num % 2 == 0:
        if num % 5 == 0:
            print(f"{num} is even and divisible by 5")
        else:
            print(f"{num} is even not divisible by 5")
    else:
        if num % 5 == 0:
            print(f"{num} is odd and divisible by 5")
        else:
            print(f"{num} is odd not divisible by 5")