# Python program to convert a decimal number to octal
# Main steps are:
# 1. Store the remainder when the number is divided by 8 in an array.
# 2. Divide the number by 8
# 3. Repeat the first two steps until the number is not equal to 0
# 4. Print the array in reverse order

# We will be using functions
def decToOctal(n):
    # Array to store octal number
    octalNum = [0] * 100
    
    # Counter for Octal Number array
    i = 0
    while (n != 0):
        # Storing remainder in octal array
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    # Printing octal number array in reverse order
    for j in range(i -1, -1, -1):
        print(octalNum[j], end="")

# code - change n to the decimal number required
n = 63
# Function call
decToOctal(n)
