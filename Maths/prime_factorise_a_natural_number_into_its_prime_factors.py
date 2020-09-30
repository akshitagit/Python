import math

# This is used to set our input range as we will be initalizing our 
# smallest prime factor array till that number.
# Setting it to the standard 10^7 size input
max_num = 10000001

# This is used to initalize our array.
small_prime_fact = [0 for i in range(max_num)] 

# This function is used to find and initalize the smallest prime factor of all the numbers in the range
def main_func(): 
	small_prime_fact[1] = 1
	for i in range(2, max_num):  
		small_prime_fact[i] = i 
	
    # Initalizing all the even numbers smallest prime factor to 2
	for i in range(4, max_num, 2): 
		small_prime_fact[i] = 2

    # This is the main loop in which we will find the smallest prime factor of all the odd numbers.
    # In this I have first found out that if a number itself is it's own smallest prime factor.
    # After that if it is then I have assigned all the other multiples of that number to this current number.
    # Going till the squareroot of the largest numbers because of the fact that
    # The largest number which could be the prime factor of a number is it's own squareroot
	for i in range(3, math.ceil(math.sqrt(max_num))): 
		if (small_prime_fact[i] == i): 
			for j in range(i * i, max_num, i): 
				if (small_prime_fact[j] == j): 
					small_prime_fact[j] = i 

# The work of this function is to divide the number by it's smallest prime factor and store the result
# in a list or an array and return that. This returned array will be our answer. 
def factorize(num): 
	factors = [] 
	while (num != 1): 
		factors.append(small_prime_fact[num]) 
		num = num // small_prime_fact[num] 
	return factors 

# Main Code

main_func()
print("Please enter the number in the range < 10^7") 
num = int(input())
facts = factorize(num)
print(f"The given prime factors of the {num} are {*facts,}")