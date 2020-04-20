t=int(input())
for b in range(t):
    n,k=map(int,input().split())
    l=[i+1 for i in range(n)]
    v=1
    while len(l)!=1:
        if k>0:
            k-=1
            v=v+2
            while v>len(l):
                v=v-len(l)
        if k==0:
            while v>=len(l):
                v=v-len(l)
            l.pop(v)
            v=v+2-1
            while v>=len(l):
                v=v-len(l)
            
            
    print(l[0])
