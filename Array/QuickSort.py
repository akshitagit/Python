
class QuickSort():
    arr = []
    def __init__(self, arr):
        self.arr = arr
        self.quickSort(self.arr, 0, len(arr) - 1)

    def doPartition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1

        for n in range(low, high):
            if(arr[n] <= pivot):
                i = i + 1
                arr[i], arr[n] = arr[n], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr

        if(low < high):
            pivot = self.doPartition(arr, low, high)
            self.quickSort(arr, low, pivot - 1)
            self.quickSort(arr, pivot + 1, high)

    def printSortedArray(self):
        print(self.arr)

quick_sort = QuickSort([100, 20, 50, 11, 415, 12, 56])
quick_sort.printSortedArray() # PRINTS => [11, 12, 20, 50, 56, 100, 415]
