rows = 5

for i in range(rows + 1):
  for j in range(rows - i):
    print(" ", end=" ")
  for j in range(i):
    print("*", end=" ")
  print(" ")
