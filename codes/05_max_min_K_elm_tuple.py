tuple1 = (20, 4, 15, 22, 57, 7, 8)
k = 3

sorted_tuple = sorted(list(tuple1))
max_k_elm = sorted_tuple[-k:]
min_k_elm = sorted_tuple[:k]

print(tuple(min_k_elm+max_k_elm))
