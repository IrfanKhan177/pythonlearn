n= 6
print("Guess the number...")
i=0
while(True):
    if i==6:
        print("You Loose")
        print("You can guess only 6 times")
        break
    a=int(input())
    if a<=10 and a>6:
        i=i+1
        print("Guess the near and lower number which you inputed...")

    elif a>10:
        i=i+1
        print("Guess a lower number...")
    elif a<6 and a>=3:
        i=i+1
        print("Guess the near and higher number which you inputed...")
    elif a<3:
        i=i+1
        print("Guess a higher number...")
    
    elif a==n:
        i=i+1
        print("Game over!")
        print("You completed the game with",i,"times of guesses")
    