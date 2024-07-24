tup = (1, 2, 76, 342, 32, "green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

countries=("Spain","Italy","india","England","Germany")
newlist=list(countries)
newlist.append("Russia")
newlist.pop(3)
newlist[2]=("Canada")
countries=tuple(newlist)
print(countries)

countries1=("Pakistan","Africa","America","Mexico")
countries2=("Japan","Singapore","Thailand")
allcountries=countries1+countries2
print(allcountries)