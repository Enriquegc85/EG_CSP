#EG, reading and writting to file

with open("prctice.txt", "r+") as file:
    content = file.read()
    content = "Chapter 1:\n" + content + "\nAnd chris robin was sititng on his doorstep putting on his big boots"
    file.write(content)

with open("prctice.txt", "a") as file:
    file.write("\nWinnie the pooh and the blusterry day")
