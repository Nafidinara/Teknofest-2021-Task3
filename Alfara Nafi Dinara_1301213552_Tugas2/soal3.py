# input = ['js', 'js', 'golang', 'ruby', 'ruby', 'js', 'js']
input = ['danu', 'danu', 'alif', 'indra', 'indra', 'kurniadi', 'indra']

newList = []

[newList.append(item) for item in input if item not in newList]

for x in newList:
    print(x,' : ',input.count(x))