# Python sorting program by using Selection Sort

print("Enter the space seperated numbers which you want to sort\n")
array = list(map(int,input().split()))

#traversing elements
for elm in range(len(array)):
    min_elem = elm
    #check remaining unsorted elements 
    for nxt_elm in range(elm + 1, len(array)):
        if(array[min_elem]>array[nxt_elm]):
            min_elem = nxt_elm
    
    #swap minimum elem with the first element
    array[elm],array[min_elem] = array[min_elem],array[elm]

print("Your sorted array is:\t")
print(*array)