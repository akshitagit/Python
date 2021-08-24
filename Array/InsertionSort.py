
class InsertionSort():
    arr = []
    def __init__(self, arr):
        self.arr = arr
        self.doSorting()

    def doSorting(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i-1
            while j >=0 and key < self.arr[j] :
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
    
    def printSortedArray(self):
        print(self.arr)

insertion_sort = InsertionSort([100, 20, 50, 11, 415, 12, 56])
insertion_sort.printSortedArray() # PRINTS => [11, 12, 20, 50, 56, 100, 415]