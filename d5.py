list = ["apple","orange","red"]
for item in list:
    print(item)
list1 = [["apple",1],["orange",4],["red",4]]
for item,con in list1:
    print(item ,"have",con)

dict1 = dict(list1) #it will convert the list into a dictionary
print(dict1) #out: {'apple': 1, 'orange': 4, 'red': 4}
# print(dict1.items())
for item,con in dict1.items():
     print(item ,"have",con)

for item in dict1:
    print(item) #it will print keys

#quizze 

lis = ["apple",34,8,"red",2,6,"pc",1]

for item in lis:
    if str(item).isnumeric() and item>=6:
        print(item)

#whileloop
i=0
while(i<23):
    i=i+1 
    print(i)

while(i<23):
    
    print(i)
    i=i+1 
while(True):
    if i==5:
        i=i+1
        continue
    print(i)
    i=i+1
    if i==55:
        i=i+1
        break

while(True):
    print("Enter your number")
    num = int(input())
    if num>100:
        print("You type greater than 100")
        break
    else:
        print("Try again")
        continue
    
    