list = [49,23,15,18,63,19]
def partition(list,start,end):
    pivot = list[start]
    c = 0
    for i in range(start,end+1):
        if list[i]<pivot:
            c += 1
    index = start+c
    list[start]=list[index]
    list[index]=pivot
    i = start
    j = end
    while(i<j):
        if list[i]<=pivot:
            i+=1
        elif list[j]>pivot:
            j-=1
        else:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
            i+=1
            j-=1
    return index 

def quickSort(list,start,end):
    if start >= end:
        return 
    pivot_index = partition(list,start,end)
    quickSort(list,start,pivot_index-1)
    quickSort(list,pivot_index+1,end)

quickSort(list,0,len(list)-1)
print(list)