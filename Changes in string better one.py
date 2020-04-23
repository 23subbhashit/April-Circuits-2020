def allah(x,l,b,c1):
    res=999999999
    c=0
    i=0
    a=list(b)
    while ''.join(a)!=c1:
        a[i]="A"
        p=''.join(a)
        for j in range(len(p)):
            if j==x:
                res=0
                return res
            else:
                if p[j]!=x[j]:
                    c=c+1
                  
        res=min(res,c)
        c=0
        if i<len(a):
            i=i+1
        else:
            pass
    return res
t=int(input())
for _ in range(t):
    n=int(input())
    sub=list(input())
    l=[]
    b="B"*len(sub)
    c="A"*len(sub)
    l.append(b)
    if n==1:
        print(0)
    elif ''.join(sub)==b:
        print(0)
    else:
        res1=allah(sub,l,b,c)
        print(res1)
