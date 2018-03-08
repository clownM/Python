from random import randint

num = randint(0,100)

print("Guess What I think?")

temp = False

while temp == False:
    inputNum = int(input())
    if inputNum < num:
        print("The number you guess is too small!")
    if inputNum > num:
        print("The number you guess is too big!")
    if inputNum == num:
        temp = True
        print("Bingo!")
