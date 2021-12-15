input = [1,2,3,4,6]
target = 6
newList = []

for x in range(len(input)):
    for i in range(len(input)):
        if input[x] + input[i] == target and input[x] != input[i]:
            newList.append(input.index(input[x]))

print(newList)