import math as m
# maths in build moodule having function likes square root , log , exponent ,power and many more


# Function defination
def prime_factor(number):

    # this will check if number is 1 and 0 it will tell the user that that both zero or 1 both are not prime factor as prime factor are always greater then 1
    if number==1 or number==0:
        print(f"{number} is not having prime factor .Prime factors are always greater then two.Enter number a greater than equal two(2)")
    # The while loop will run if the number is divisble by 2(condition true) and remainder(checked using % operator) is 0

    else:
        print(f"Prime Factors of {number} is/are")
        while number%2==0:
            print(2,end=" ")
            number=number/2

        #This loop is used for odd numbers and skip it by 1
        #sqrt is used to find square root of function
        #here for example number is 25 condition in for loop : Entered i =3 range(3,6,2) i will have values 3 5


        for i in range(3,int(m.sqrt(number))+1,2):

            #here checking if number is completely disible by i
            while number % i == 0:
                print (i,end=" ")
                number = number / i

    #Here if condition checking for prime factors!!
        if number > 2:
            print(int(number),end=" ")


#Inputing a number to check its Prime factors
number = input("Enter a number to find its Prime Factors :  ")

    # Calling function prime_factor by passing an argument number
    #Here Try and Expect block checking if type of number is interger or not
try:
    #here if condition checking if number is negative or positive
    if int(number) > -1:
        prime_factor(int(number))
    else:
        print(f"{number} is Negative . And Negative numbers are not natural number!!They are Intergers")

except ValueError:
    print(f"Try with natural numbers!")
