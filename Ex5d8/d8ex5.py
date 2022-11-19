client =["harry","rohan","hammad"]
action =["food","exer"]
def getdate():
    import datetime
    return datetime.datetime.now()
def log(clname,logn):
    
    clstr = clname+logn+".txt"
    with open(clstr,"a") as f:
        print("Enter Your Log")
        cont = input()
        content= str(getdate())+" ---> "+cont+"\n"
        print(content)
        f.write(str(content))
        print("You successfully logged")
def retrieve(clname,logn):
    
    clstr = clname+logn+".txt"
    with open(clstr,"r+") as f:
        print("Your Result")
        
        print(f.read())
l = True
while l:
    print('''
    0 - Harry
    1 - Rohan
    2 - Hammad
    ''')
    clno = int(input())
    clname = str(client[clno])
    print('''
    What do you want?
    1 - log
    2 - retrive
    ''')
    act = int(input())
    if act == 1:
         print("What you want to log- Diet or Exercise")
         print("0 - Diet")
         print("1 - Exercise")
         dec = int(input())
         logn = str(action[dec])
        
         log(clname,logn)
         
         
    elif act == 2:
         print("What you want to log- Diet or Exercise")
         print("0 - Diet")
         print("1 - Exercise")
         dec = int(input())
         logn = str(action[dec])
        
         retrieve(clname,logn)
    print("Do you want continue?Y/N")
    ex = input()
    if ex == "Y" and "y":
       continue
    elif ex == "N" and "n":
       exit()
         
         


         
         


