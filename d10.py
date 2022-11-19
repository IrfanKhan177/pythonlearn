# def minus(x,y):
#     return x-y

# print(minus(5,1))

# minus = lambda x , y : x-y
# print(minus(6,2))
# def srt(a):
#     return a[0]
# a = [[1,4],[4,6],[3,2]]
# a.sort(key=srt)
# print(a)
# a = [[1,4],[4,6],[3,2]]
# a.sort(key=lambda a: a[0])
# print(a)

import random

nm = random.randint(0,6)
print(nm)
rng = random.random()*100
print(rng)
lst = ["One","Four","Ten"]
rng = random.choice(lst)
print(rng)
#String Formating
ni = "He is a good boy"
me = "Irfan."
# a = "This is %s"%me
# a = "This is %s %s"%(me,ni) #In first percent it will print me variable and second variable it will print ni variable
# a = "This is {} {}"
a = "This is {1} {0}" 
# b=a.format(me)
# b=a.format(me,ni) #In a variable where is 0 it will print me and where is 1 there will print ni because it will print by index of b variable
# print(b)
a = f"This is {me} {ni}" 
print(a)