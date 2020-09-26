# TRIANGLE PATTERN

'''
input : 4

output : 

      1 
    2 3 2
  3 4 5 4 3
4 5 6 7 6 5 4

'''

if __name__ =='__main__':
    n = int(input())
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(end='  ')

        flag=0
        for j in range(i):
            print(i+flag,end=' ')
            flag+=1
        
        flag1 = i-2
        for j in range(i+1,2,-1):
            print(j+flag1-1,end=' ')
        print()
