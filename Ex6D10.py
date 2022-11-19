import random
el = ["snake","water","gun"]
cp =0
hp =0
while True:
    if cp==5:
        print(f"Finale winner is computer with {cp} ")
        print(f"And you loose with computer with {hp}")
        break
    elif hp==5:
        print(f"Finale winner is you with {hp} ")
        print(f"And computer loose with you with {cp}")
        break
    print("""
    s - snake
    w - water
    g - gun 
    Type one...
    """)
    uinp= input()
    pinp= random.choice(el)
    if uinp == "s" and pinp == "water":
        print("You choose snake")
        print(f"Computer choose {pinp}")
        print("You win!")
        hp = hp+1
        print(f"Your point {hp} and computer point {cp}")
    elif uinp == "w" and pinp == "snake":
         print("You choose water")
         print(f"Computer choose {pinp}")
         print("You loose!")
         cp = cp+1
         print(f"Your point {hp} and computer point {cp}")
    elif uinp == "g" and pinp == "snake":
         print("You choose gun")
         print(f"Computer choose {pinp}")
         print("You win!")
         hp = hp+1
         print(f"Your point {hp} and computer point {cp}")
    elif uinp == "s" and pinp == "gun":
         print("You choose snake")
         print(f"Computer choose {pinp}")
         print("You loose!")
         cp = cp+1
         print(f"Your point {hp} and computer point {cp}")
    elif uinp == "g" and pinp == "water":
         print("You choose water")
         print(f"Computer choose {pinp}")
         print("You loose!")
         cp = cp+1
         print(f"Your point {hp} and computer point {cp}")
    elif uinp == "w" and pinp == "gun":
         print("You choose gun")
         print(f"Computer choose {pinp}")
         print("You win!")
         hp = hp+1
         print(f"Your point {hp} and computer point {cp}")
    elif uinp == "s" and pinp == "snake":
         print("You choose snake")
         print(f"Computer choose {pinp}")
         print("Draw")
         print(f"Your point {hp} and computer point {cp}")
    elif uinp == "w" and pinp == "water":
         print("You choose water")
         print(f"Computer choose {pinp}")
         print("Draw")
         print(f"Your point {hp} and computer point {cp}")
    
    elif uinp == "g" and pinp == "gun":
         print("You choose gun")
         print(f"Computer choose {pinp}")
         print("Draw")
         print(f"Your point {hp} and computer point {cp}")
    

    else:
        
        print("Choose valid carecter")