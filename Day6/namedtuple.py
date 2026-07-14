from collections import namedtuple
student=namedtuple('student',['name','age', 'grade'])
s1=student('Ravi', 20, 'A')
print(s1.name)
print(s1.age)
print(s1.grade)