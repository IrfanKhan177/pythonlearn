

print("Which operation do you want:")
print('''
+ -- Addition
- -- Subtraction
* -- Multiplication
/ -- Divide

'''
)

op = input("Enter following one..\n")
if op == '+':
    print("Enter your first number:")
    a = int(input())
    print("Enter your first number:")
    b = int(input())
    if a==56:
        print("Your answer is ",77)
    elif b==9:
        print("Your answer is ",77)
    elif a==9:
        print("Your answer is ",77)
    elif b==56:
        print("Your answer is ",77)
    else:
        print("Your answer is",a+b)
elif op == '*':
    print("Enter your first number:")
    a = int(input())
    print("Enter your first number:")
    b = int(input())
    if a==45:
        print("Your answer is ",555)
    elif b==3:
        print("Your answer is ",555)
    elif a==3:
        print("Your answer is ",555)
    elif b==45:
        print("Your answer is ",555)
    else:
        print("Your answer is",a*b)
elif op == '/':
    print("Enter your first number:")
    a = int(input())
    print("Enter your first number:")
    b = int(input())
    if a==56:
        print("Your answer is ",4)
    elif b==6:
        print("Your answer is ",4)
    elif a==6:
        print("Your answer is ",4)
    elif b==56:
        print("Your answer is ",4)
    else:
        print("Your answer is",a/b)
elif op == '-':
    print("Enter your first number:")
    a = int(input())
    print("Enter your first number:")
    b = int(input())
    print("Your answer is",a-b)
else:
    print("Invelid oparation")



