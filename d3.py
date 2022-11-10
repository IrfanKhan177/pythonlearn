mstr = "Irfan is a good boy"
print(mstr)
print(mstr[4])#out: n
print(mstr[0:5])
print(len(mstr))
print(mstr[0:19])
print(mstr[0:78])
print(mstr[0:5:2]) #afteer second : value will skip 1 carecter
print(mstr[:]) #before : it will give automatically index of 0 and after : it will give it's length
print(mstr[:5])#before : it will give automatically index of 0
print(mstr[::])#brfore first : it will give automatically index of 0 and before second : it will give it's length and after second :  it will give default 1
print(mstr[-4:]) 
print(mstr[::-1]) #it will be reverse
print(mstr[::-2]) #it will be reverse and skib 1 by 1 caracter

#some function

print(mstr.isalnum()) #it returns false because this string has spaces
# it will return true in without space string

print(mstr.isalpha()) #it returns false because this string has spaces
# it will return true in without space string

print(mstr.endswith('boy'))
print(mstr.count('o')) #it returns how much o in this string
print(mstr.capitalize()) #it will be capitalized first carecter of this string
print(mstr.find('is')) #is index start from 6
print(mstr.replace('is','are'))


# LIST 

list1 = ["Apple",12,"12",True,False,[4,7]]
print(list1)
print(list1[5][0])

num=[5,8,2,78]
num.sort() #it will sort this list
num.reverse()#It will reverse the list
num.append(45) # it will be add 45 in the end of this list
num.insert(1,50) # it will insert 50 in the index of 1 
#syntex list.append(index,value)
num.remove(5) #it will remove 5 from this list
num.pop() #it will remove last number from this list
num[3]=89 #it will update the index of this list
print(num)
print(len(num))
print(max(num))#maximum number of this list
print(min(num))#minimum number of this list

#Tuples

tp =(1,9,True)
print(tp)