# Program to check if a number is prime or not

#input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than or equal to 1
else:
   print(num,"It's not a prime number")
