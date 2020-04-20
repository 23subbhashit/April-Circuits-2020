'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def right(a,b):
    r=a
    for i in range(b):
        r=r[-1:]+r[:-1]
    r=''.join(r)
    return int(r)
def left(a,b):
    r=a
    for i in range(b):
        r.append(a.pop(0))
    r=''.join(r)
    return int(r)
def btod(n):
    if n==0:
        return 0
    return n%10+2*(btod(n//10))
for i in range(int(input())):
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    a=bin(a)
    a=a[2:]
    a=str(a)
    if (16-len(a))!=0:
        a="0"*(16-len(a))+a
    a=list(a)
    if c=='L':
        res=left(a,b)
        res=btod(res)
        print(res)

    if c=='R':
        res=right(a,b)
        res=btod(res)
        print(res)

    
