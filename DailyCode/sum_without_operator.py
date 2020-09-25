def Add(x, y):

    while (y != 0):

        carry = x & y

        x = x ^ y

        y = carry << 1

    return x

val1 = int(input())
val2 = int(input())

print(Add(val1, val2))