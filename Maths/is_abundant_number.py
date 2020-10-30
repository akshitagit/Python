# In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself. The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16.
def isAbundant(n):
    fctr_sum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctr_sum > n


print(isAbundant(12))
print(isAbundant(13))
