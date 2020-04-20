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
    print(a)
    a=a[2:]
    a=str(a)
    if len(a)%4!=0:
        a="0"*(4-len(a)%4)+a
    print(a)
    a=list(a)
    if c=='L':
        res=left(a,b)
        res=btod(res)
        print(res)

    if c=='R':
        res=right(a,b)
        res=btod(res)
        print(res)
