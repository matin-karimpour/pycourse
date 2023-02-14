list1 = [1,2,3,4,5]
list_of_tuples = []

for i in list1:
    list_of_tuples.append((i,i**3))

print(list_of_tuples)

list_of_tuples2 = [ (i, i**3) for i in list1]
print(list_of_tuples2)