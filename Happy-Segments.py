'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,m=map(int,input().split())
a=[int(x) for x in input().split()]
b=[int(x) for x in input().split()]
t=int(input())
for i in range(t):
    l,r=[int(x) for x in input().split()]
    arr=a[l-1:r]
    un=list(set(arr))
    c=0
    for i in un:
        if i not in b:
            pass
        if i==arr.count(i):
            c=c+1
    if c==len(un):
        print(1)
    else:
        print(0)
