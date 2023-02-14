# Counting the frequencies in a list using dictionary in Python

list1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

dict1 = {}
for i in list1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)

dict2 = {}
for i in list1:
    dict2[i] = dict2.get(i,0) + 1
print(dict2)