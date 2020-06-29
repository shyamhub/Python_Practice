def bubble_sort(sequence):
    lenght = len(sequence)
    #print("Lenght of Sequence ",lenght)

    if(lenght <=1):
        return sequence

    for item in range(1,lenght):
        for item in range(0,lenght-1):
            if sequence[item] < sequence[item+1]:
                continue
            else:
                sequence[item] , sequence[item+1] = sequence[item+1], sequence[item]
    return bubble_sort(sequence)

sorted_list = bubble_sort([2,1,4])
print(sorted_list)