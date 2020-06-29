def quick_sort(sequence):
    length = len(sequence)
    if length <=1:
        return sequence
    else:
        pivot = sequence.pop()
        #print(pivot)

    larger_pivot = []
    smaller_pivot = []

    for item in sequence:
        if item > pivot:
            larger_pivot.append(item)
        else:
            smaller_pivot.append(item)
    return quick_sort(smaller_pivot) + [pivot] +quick_sort(larger_pivot)



sorted_list= quick_sort([2,6,3,4,9,23,54,45])
print(sorted_list)