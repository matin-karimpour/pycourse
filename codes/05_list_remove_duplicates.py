def remove_duplicates(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

x = input("please input your data: ")
x = x.split()
y = remove_duplicates(x)
print(y)