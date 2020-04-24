from sys import stdin
t=int(stdin.readline())
for _ in range(t):
    n=int(stdin.readline())
    sub=list(input())
    if n==1:
        print(0)
        
    else:
        res=10**10
        
        for  i in range(n):
            u=sub[:i+1]
            v=sub[i+1:]
            right=u.count('B')+v.count('A')
            res=min(res,right)
    print(res)
