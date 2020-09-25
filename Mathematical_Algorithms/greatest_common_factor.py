# Uses the Euclidean algorithm to compute the greatest common factor between 2 integers.
def gcf(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcf(num2, num1 % num2)