from sys import stdin,stdout
import bisect
#a=[10,11,20]
#print(bisect.bisect_right(a,12))
for _ in range(1):
	#n,shift,ch=stdin.readline().split()
	m,n=map(int,stdin.readline().split())
	gp=sorted(map(int,stdin.readline().split()))
	a=sorted(map(int,stdin.readline().split()))
	if gp[-1]>a[-1]:stdout.write('-1\n')
	else:
		ind=m;pos=[]
		for i in range(n-1,-1,-1):
			ind=bisect.bisect_right(gp[:ind],a[i])-1
			if ind==-1:break
			pos+=[ind]
		ans=0
		#print(pos)
		for v,v1 in zip(pos,pos[1:]):
			ans=max(ans,v-v1)
		ans=max(ans,pos[-1]+1)
		print(ans*2-1)
