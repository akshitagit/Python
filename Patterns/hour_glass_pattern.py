def hour_glass_pattern(n):

    # loop for printing the upper half
    for i in range(n+1):
        
        # printing the spaces at the beginning
        for k in range(i):
            print(" "*2, end="")
        
        # printing the values in each row
        for j in range(-(n-i), (n-i+1)):
            print(abs(j), end=" ")

        print()

    # Loop for printing the lower half
    for i in range(1, n+1):
        
        # Printing spaces at the beginning
        for k in range(n-i):
            print(" "*2, end="")
        
        # Printing values in each row
        for j in range(-i, i+1):
            print(abs(j), end=" ")

        print()


n = int(input("Enter the number of rows : "))
hour_glass_pattern(n)
