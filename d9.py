l=10 #It is a global variable
def func1():
    print(l)
func1()

l=10 #It is a global variable
def func1():
    l=5 # It is a local variable/It can't change the global variable value
    print(l) #It will search variable first in local is variable is not exist in local it will cheack in global
func1()
print(l)
l=10 #It is a global variable
def func1():
    global l #It make l variable local to global variable
    l=5 # Now it is global and it updated l variable
    print(l) #It will search variable first in local is variable is not exist in local it will cheack in global
print("Before function calling",l)
func1()
print("after function calling",l)#After function calling it updted l value
def fun():
    x=20
    def fun2():
         global x
         x= 88
    print("before calling fun2",x)
    fun2()
    print("After calling fun2",x) #Before and after calling fun2 return x value 20 because this will not cheack or update under it's scope or in neted function
fun()
print(x) #out: 88 because it will make this variable and return
x=70
def fun():
    x=20
    def fun2():
         global x
         x= 88
    print("before calling fun2",x)
    fun2()
    print("After calling fun2",x) #Before and after calling fun2 return x value 20 because this will not cheack or update under it's scope or in neted function
fun()
print(x) #out: 88 because after calling this function this variable updated



#https://www.youtube.com/watch?v=im7Z1jKMGao&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=34

# def fact_itertative(n):
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return fac
# n = int(input())
# print(fact_itertative(n))
# print(range(4))
def fact_recursion(n):
    if n==1:
        return n
    else:
        return n*fact_recursion(n-1)

n = int(input())

print(fact_recursion(n))

