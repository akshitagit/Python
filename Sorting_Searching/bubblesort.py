# Compares the adjacent values and swapping them if they are not in the right order

def sorting(numbers):
	for j in range(len(numbers)): # repeating the loop for the number of element amount of times
		swapped = False # keep track of swapped values
		count = 0
		while count < len(numbers) - 1:
			if numbers[count] > numbers[count + 1]: # compares adjacent values
				numbers[count], numbers[count+1] = numbers[count + 1], numbers[count] # swapping the places of lower and higher value
				swapped = True
			count = count + 1
		if swapped == False:
			print("sorting")
	print(numbers)

sorting([222, 999, 1, 1.1, 54666, 333, 15, 8.678, 8.6781, 444, 99]) # testing it out 