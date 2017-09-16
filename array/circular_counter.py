"""
There are people sitting in a circular fashion,
print every third member while removing them,
the next counter starts immediately after the member is removed.
Print till all the members are exhausted.
For example:
Input: consider 123456789 members sitting in a circular fashion,
Output: 369485271
"""
import  re
array='123456789'
counter=2
l=[]
for a in array:
    l.append(a)
while 1:
    print(l[counter])
    l.pop(counter)
    if len(l)>0:
        counter=(counter+2)%len(l)
    else:
        break
