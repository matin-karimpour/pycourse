tuple1 = (1, 2, 7, 20, 46)

sum1 = 0
for i in tuple1:
    sum1 += i
print(sum1)

sum2 = sum(list(tuple1))
print (sum2)