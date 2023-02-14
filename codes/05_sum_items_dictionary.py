dictionary1 = {'a':100, 'b':200, 'c':300}

sum1 = 0
for i in dictionary1:
    sum1 += dictionary1[i]
print(sum1)


sum2 = sum(dictionary1.values())
print(sum2)


sum3 = 0
for i in dictionary1.items():
    sum3 += i[1]
print(sum3)