print("Hello")
x=1
print(x+1)
print("X+1")


a=5
b=5

print(a is b)
print (a == b)
a=[1,2,3]
b=[1,2,3]
print(a is b)


expression="10*20"
print(eval(expression))
print(expression)
a=10
b=5
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)

list1=["Mike", "John", "", "Ravi"]
relist=list(filter(None, list1))
print(relist)