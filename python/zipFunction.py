list1 = range(1, 11)
list2 = range(65, 76)
list3 = []
k = 0
for i in list2:
    list3.append(chr(i))
    k += 1
zipped = list(zip(list1, list3))
print("zipped list     ", zipped)
zipped = tuple(zip(list1, list3))
print("zipped Tuple     ", zipped)
zipped = set(zip(list1, list3))
print("zipped Set     ", zipped)
zipped = dict(zip(list1, list3))
print("zipped Dict     ", zipped)
