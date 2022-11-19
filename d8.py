f = open("d8.txt")
# print(f.tell()) #It return cursor pointer
print(f.readline())
# print(f.tell())
f.seek(12)#It will reset cursor pointer in 0 or the starting position of the file/where from it will read
print(f.readline())
# print(f.tell())
f.close()

# with open("d8.txt","r") as f:
#     a =f.read()
#     print(a)

