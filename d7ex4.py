print("Type 0 or 1")
n = int(input())
b= bool(n)
print("How much do you want")
m= int(input())
if b==True:
    i=0
    while i<m:
        i=i+1
        print("*"*i)
elif b==False:
    i=0
    list=[]
    while i<m:
        i=i+1
        list.append(i)
        list.sort(reverse=True)
    for l in list:
       print(l*"*")
        

