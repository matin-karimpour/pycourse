def sort_list(unsorted: list()):
    for i in range(len(unsorted)):
        for j in range(len(unsorted)):
            if unsorted[i] < unsorted[j]:
                unsorted[i],unsorted[j] =unsorted[j], unsorted[i]

    return unsorted
            
unsorted = [2, 4, 5 ,7,1 ,3 ,4 ,6]
print(sort_list(unsorted))
