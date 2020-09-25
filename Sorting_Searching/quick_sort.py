# Partition the list based in a pivot
def partition(sort_list, low, high):
    """
    All the elements smaller than the pivot
    will be on the left side of the list
    and all the elements on the right side 
    will be greater than the pivot. 
    """
    i = (low - 1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)


# Recursive implementation of the quicksort based on the partition
def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)


# Driver Program to show the implementation
lst = []
size = int(input("Enter size of the list : "))
for i in range(size):
    elements = int(input("Enter an element : "))
    lst.append(elements)
low = 0
high = len(lst) - 1
quick_sort(lst, low, high)
print(lst)
