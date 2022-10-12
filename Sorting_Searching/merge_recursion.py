list=[20,51,4,28,39,12,67]
def merge(s1,s2,list):
    i=0
    j=0
    k = 0
    while i<len(s1) and j<len(s2):
        if s1[i]<s2[j]:
            print(list)
            list[k] = s1[i]
            i = i + 1
        else :
            list[k] = s2[j]
            j = j + 1
        k = k+1
    while i<len(s1):
        list[k] = s1[i]
        k = k + 1
        i = i + 1
    while j<len(s2):
        list[k] = s2[j]
        k = k + 1
        j = j + 1

def mergeSort(list):
    if len(list)==0 or len(list)==1:
        return
    mid = len(list)//2
    s1 = list[:mid]
    s2 = list[mid:]
    mergeSort(s1)
    mergeSort(s2)
    merge(s1,s2,list)

mergeSort(list)
print(list)
