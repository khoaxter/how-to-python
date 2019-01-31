thislist=['apple','orange','banana']
print(thislist)
print('print at position 1')
print(thislist[1])
thislist[1]='cherry'
print('print position 1 when position 1 with another postion is cherry')
print(thislist[1])
print('print for list')
for x in thislist:
    print(x)
print('if appler in thislist')
if 'apple' in thislist:
    print('apple is fruit in thislist')
print('print lenght of thislist')
print(len(thislist))
print('append string in the thislist')
thislist.append('cherry')
print(thislist)
print('----------------')
# thislist.insert(1,'orange')
# print(thislist)
thislist.sort()
print(thislist)
# thislist.remove('banana')
# print(thislist)
# thislist.pop() # remove index specified or last index in item
# print(thislist)
# del thislist[2]
# print(thislist)
# thislist.clear()
# print(thislist)
