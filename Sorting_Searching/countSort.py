MAX = 1024


# Linear time sorting algorithm
def count_sort(arr):

    count, sorted_arr = [0 for i in range(
        MAX + 1)], [0 for i in range(len(arr))]

    # Make a hash
    for i in range(len(arr)):
        count[arr[i]] += 1

    # count frequency
    for i in range(1, MAX + 1):
        count[i] += count[i - 1]

    # a simple math to new position of element in sorted array
    for i in range(len(arr)):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return sorted_arr


# Stable algorithm for count sort
def stable_count_sort(arr):

    count, sorted_arr = [0 for i in range(
        MAX + 1)], [0 for i in range(len(arr))]

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, MAX + 1):
        count[i] += count[i - 1]

    # traverse reverse for stability
    for i in range(len(arr) - 1, -1, -1):
        sorted_arr[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return sorted_arr


# Driver Program to show the implementation
lst = []
size = int(input("Enter size of the list : "))
for i in range(size):
    elements = int(input("Enter an element : "))
    lst.append(elements)
print(stable_count_sort(lst))
