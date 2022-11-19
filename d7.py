#File IO

"""
"r" - Open file for reading - default
"w" - Open file for writing
"x" - Create file if not exist else operation will failed
"a" - Add more content to a file
"t" - text mode - default
"b" - Binarry mode
"+" - read and write

"""

# f = open("d2.txt","rt")
# content = f.read(344)
# print(content)
# content = f.read(3)
# print("2",content)
# f.close()
# f = open("d2.txt","rt")
# content = f.read()
# print(content)
# # content = f.read(3)
# # print(content)
# f.close()
# f = open("d2.txt","rt")
# for line in f:
#     print(line,end="")


# f.close()
f = open("d2.txt","rt")

print(f.readline())

# print(f.readline())
# print(f.readlines())
f.close()

# f=open("d7_2.txt","w")
# f.write("Hello, sobaike")
# f.close()

# f =open("d7_2.txt","a")
# # f.write("Hello")
# f.write("Hello\n")
# f.close()
# f= open("d7_2.txt","r+")
# print(f.read())
# f.write("HI")      
# f.close()