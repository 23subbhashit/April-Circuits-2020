n,m=map(int,input().split())
l=[int(x) for x in input().split()]
c=[0 for i in range(len(l))]
c2=[1 for i in range(len(l))]
l.sort(reverse=True)
l1=[int(x) for x in input().split()]
c1=[0 for i in range(len(l1))]
l1.sort(reverse=True)
count=0
if l[0]>l1[0]:
    print(-1)
else:
    while c!=c2:
        for i in range(len(l1)):
            for j in range(len(l)):
                if l1[i]>=l[j]:
                    if c1[i]!=1 and c[j]!=1:
                        c1[i]+=1
                        c[j]+=1
        
        c1=[0 for i in range(len(l1))]
        count=count+2
    print(count-1)

     

    
