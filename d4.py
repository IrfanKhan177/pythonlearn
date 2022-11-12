d1 = {}
print(type(d1)) #type is dict

d2 = {"irfan":"burger","kalim":"rice","rahin":"fish","marin":{"B":"roti","L":"rice"}}


print(d2) #out: {'irfan': 'burger', 'kalim': 'rice', 'rahin': 'fish'}
print(d2["irfan"])
print(d2["kalim"])
print(d2["rahin"])
print(d2["marin"]["L"])
print(d2.get("irfan")) #it will return the item of irfan
d2.update({"limon":"coffee"}) #it will add in the dict
print(d2.keys()) #it will return all keys of the dict
print(d2.items()) #it will return all items of the dict
print(d2)

d2["karin"]= "Burger" #karin will append in this dict
del d2["kalim"] # kalim will be delete from this dict
print(d2)
# d3= d2 # d2 dict will transfer in d3
# d3["hh"]="hh" #it will also  change the d2 dict
# print(d2)

# d4 = d2.copy()  #it will make a copy of d2
# d4["gj"]="gh" #it will not change the value of d2
# print(d2)
# print(d4)


#SET

s=set()
print(type(s)) #the type of s is set
s.add(1) #set always add unique value
s.add(1)
s.add(2)
s.union({1,2,3})
s.remove(2) #it will remove 2 from this set
print(s)
s_from_list = set([1,2,4])
print(s_from_list)
lis = [1,2,3,4,5]
l_s = set(lis)
print(l_s)

#if else

var1 = 6
var2 = 56
var3 = int(input())
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

list = [3,6,4]
print(6 in list) # return true
print(5 in list) # return false
print(5 not in list) # return true
if 6 in list:
    print("Available")
