global size

def linearSearch(arr,find):
    for i in range(size):
        if arr[i] == find:
            print("Element is found at " + str(i) + "Index\n")
            print("\n Note: - Element start from 0 index")
            break
    else:
        print("Element is not found in entire array\n")    


if __name__ == "__main__":

    size = int(input("Enter a size of the array\n"))

    array = []
    print("Enter the element of the array\n")

    for i in range(size):
        temp = int(input())
        array.append(temp)

    search = int(input("Enter a element to be searched\n"))
    linearSearch(array, search)    