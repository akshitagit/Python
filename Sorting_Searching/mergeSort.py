
# -*- coding: utf-8 -*-
def mergeSort(array):
    if len(array)>1:
        
        #dividing array into 2 parts
        middle=len(array)//2
        leftArray=array[:middle]
        rightArray=array[middle:]
        
        #recursively calling MergeSort
        mergeSort(leftArray)
        mergeSort(rightArray)
        
        #3 variables for copying the sorted values into final array
        i=j=k=0
        #copying into final array
        while i<len(leftArray) and j<len(rightArray):
            if leftArray[i]<rightArray[j]:
                array[k]=leftArray[i]
                i+=1
            else:
                array[k]=rightArray[j]
                j+=1
            k+=1
            
        #checking for any elements still left
        while i<len(leftArray):
            array[k]=leftArray[i]
            i+=1
            k+=1
        
        while j<len(rightArray):
            array[k]=rightArray[j]
            j+=1
            k+=1
        
