file=open('student.txt','r')
data=file.read()
print(data)
file.close()

file=open('student.txt','a+')
file.write("This is a new line of text.\n")
file.write("This is another line of the file.\n")
file.seek(1) #move the cursor pointer to the beginning
data=file.read()
print(data)
file.close()


# file=open('student.txt','r')
# data=file.read()
# print(data)
# file.close()


