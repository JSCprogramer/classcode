#making lists fo lab 1#

names1=["Alex","Nina","John","Jackie"]
names2=["Zack","Mary"]

print("List1:", names1)
print("List2:", names2)

print("Number of elementsin list 1:",len(names1))
print("Number of elements in list 2:",len(names2))

JackieIndex = names1.index("Jackie")
print ("JackieIndex:", JackieIndex)

print("Second element of list 1",names1[1])
print("Second element of list 2",names2[1])

print("last element of list 1",names1[-1])
print("last element of list 2",names2[-1])

NinaTime=names1.count("Nina")
print("Nina times:", NinaTime)

names1.append("James")
print('List1:', names1)

names2.append('friendname')
print('List2:', names2)

names1.extend(names2)
print('List1',names1)
print('List2',names2)

names1.insert(0,'EGT267')
print("list1:", names1)

del names2[0]
print("List 2:", names2)

del names1[1:6]
print('List 1:', names1)

names1.sort()
print('List 1:', names1)

List1=sorted(names1)
print('Lists 1:', names1)


sorted(names1, reverse=True)
print('list1:', names1)
