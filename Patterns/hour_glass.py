n = int(input("Enter the value of N: "))

for i in range(n, -1, -1):
	for _ in range(n-i):
		print(" ", end=" ")

	for j in range(i, -1, -1):
		print(j, end=" ")

	for j in range(1, i+1):
		print(j, end=" ")

	print()


for i in range(1, n+1):
	for _ in range(n-i):
		print(" ", end=" ")

	for j in range(i, -1, -1):
		print(j, end=" ")

	for j in range(1, i+1):
		print(j, end=" ")

	print()
