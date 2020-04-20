'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def ind(a):    
    index=0
    c=0
    res=0
    for i in range(len(a)):
        if a[i] == 'A':
            c=c+1
        if a[i] == 'B':
            if c>=res:
                res=c;
                index=i-1
                c=0
    if c>=res:
        index=i
    return index

def outbt(n,l):
    count=0
    if n+1==len(l):
        for i in range(n):
            if l[i] == 'B':
                count+=1
    else:
        for i in range(n):
            if l[i] == 'B':
                count+=1
        for i in range(n+1,len(l)):
            if l[i] == 'A':
                count+=1
    return count
t=int(input())
for i in range(t):
    n=int(input())
    sub=list(input())
    if n==1:
        print(0)
    else:
        res=ind(sub)
        res2=outbt(res,sub)
        print(res2)

