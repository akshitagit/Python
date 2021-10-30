def maxSubArraySum(a,size):
	
	max_so_far = a[0]
	max_ending_here = 0
	
	for i in range(0, size):
		max_ending_here = max_ending_here + a[i]
		if max_ending_here < a[i]:
			max_ending_here = a[i]
		
		
		elif (max_so_far < max_ending_here):
			max_so_far = max_ending_here
			
	return max_so_far

a=[int(x) for x in input().split()]
print(maxSubArraySum(a,len(a)))
