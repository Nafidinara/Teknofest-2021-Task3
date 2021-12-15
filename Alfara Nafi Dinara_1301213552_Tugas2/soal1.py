# input = "76523752"
input = "1234123"

list = []
newList = []
for x in range(len(input)):
    list.append(int(input[x]))

for y in list:
    if list.count(y) == 1 :
        newList.append(int(y))

print(newList)