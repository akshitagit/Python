#take input from the user
input_str =  input("Enter the string: ")

#defiene the function
def rev_string(string):
	string = string[::-1]
	return string

#call the reverse function
print(rev_string(input_str))
