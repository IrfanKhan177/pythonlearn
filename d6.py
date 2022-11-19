# Operators in python

# Arithmatic operator
# Assigment operator
# Comparison operator
# Logical operator
# Identity operator
# Membership operator
# Bitwise operator

# Arithmatic operator
print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5**6 is",5**6) #it will return 5 to the power 6
print("5/6 is",5/6) #it will divide
print("5//6 is",5//6) #it will divide and never return float
print("5%6 is",5%6) #it will return reminder

# Assigment operator

# print("Assigment operator")
# x=5
# print(x)

# x+=4 #4 will add with x
# print(x)
# x=5
# x-=4 #4 will add with x
# print(x)
# x=5
# x/=4 #4 will add with x
# print(x)
# x=5
# x //=4 #4 will add with x
# print(x)
# x=5
# x **=4
# print(x)
# x=5
# x %=4 #4 will add with x
# print(x)

# Comparison operator
# print("Comparison operator")

# i=5
# print(i==5)#True
# print(i==6)#True
# print(i!=5)#False
# print(i<5)#False
# print(i<=5)#True
# print(i>5)#False
# print(i>=5)#True
# print(i and 5)#True

#Logical Operator

# a= True
# b = False

# print(a and a) #True and True = True
# print(a and b) #True and False = False
# print(b and a) #False and True = False
# print(b and b) #False and False = False

# print(a or a) #True and True = True
# print(a or b) #True and False = True
# print(b or a) #False and True = True
# print(b or b) #False and False = False

#Identity Operator
# a= True
# b = False
# print(a is b) #False
# print(5 is 6) #False
# print(a is a) #True
# print(5 is 5) #True
# print(a is not a) #False
# print(5 is not 5) #False
# print(a is not b) #True
# print(5 is not 6) #True

#Membership operator
# list = [34,33,23,66]
# print(33 in list) #True
# print(36 in list) #False
# print(33 not in list) #False
# print(36 not in list) #True



#short hand if else 
m = 6
n = 5

# if m<n : print("m is greater than n")

#...
print("m is greater than n ") if m>n else print("n is greater than m ")
print("n is greater than m") if m<n else print("m is greater than n")

#Function
print(sum((4,4)))
def function():
    print("Hello World")
function()

# def function2(a,b):
#     avg = (a+b)/2
#     return avg

# av = function2(2,3)
# print(av)

#Doc string

def function2(a,b):
    """This is a function that returns a avg"""
    avg = (a+b)/2
    return avg

av = function2(2,3)
print(av)
print(function2.__doc__)
#try except

# num1 = input("Enter first num")    
# num2 = input("Enter second num")   

# try:
#     print("Total",
#     int(num1)+int(num2))
# except Exception as e:
#     print(e)
# # except:
# #     pass
# print("jhgjhjh")

