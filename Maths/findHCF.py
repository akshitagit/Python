#  LANGUAGE: Python 3.8

def find_hcf(x, y):     #function for find hcf of two numbers
    while (y):
        x, y = y, x % y
    return x


if __name__ == '__main__':      #main function

    N = int (input())
    lst = input().split()
    num_list = list(map(int,lst))

    if (N ==1):
        hcf = num_list[0]
    else:
        num1 = num_list[0]
        num2 = num_list[1]
        hcf = find_hcf(num1, num2)

        if(N>2):
            for i in range(2, N):
                hcf = find_hcf(hcf, num_list[i])

    print (hcf)



