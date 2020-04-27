from collections import defaultdict 
pathSrcToDest=[]
class Heap(): 
 
  def __init__(self): 
    self.array = [] 
    self.size = 0
    self.pos = [] 
 
  def newMinHeapNode(self, v, dist): 
    minHeapNode = [v, dist] 
    return minHeapNode 
 
  def swapMinHeapNode(self,a, b): 
    t = self.array[a] 
    self.array[a] = self.array[b] 
    self.array[b] = t 
 
 
  def minHeapify(self, idx): 
    smallest = idx 
    left = 2*idx + 1
    right = 2*idx + 2
 
    if left < self.size and self.array[left][1] < self.array[smallest][1]: 
      smallest = left 
 
    if right < self.size and self.array[right][1] < self.array[smallest][1]: 
      smallest = right 
 
 
    if smallest != idx: 
 
 
      self.pos[ self.array[smallest][0] ] = idx 
      self.pos[ self.array[idx][0] ] = smallest 
 
      self.swapMinHeapNode(smallest, idx) 
 
      self.minHeapify(smallest) 
 
 
  def extractMin(self): 
 
 
    if self.isEmpty() == True: 
      return
 
 
    root = self.array[0] 
 
 
    lastNode = self.array[self.size - 1] 
    self.array[0] = lastNode 
 
 
    self.pos[lastNode[0]] = 0
    self.pos[root[0]] = self.size - 1
 
 
    self.size -= 1
    self.minHeapify(0) 
 
    return root 
 
  def isEmpty(self): 
    return True if self.size == 0 else False
 
  def decreaseKey(self, v, dist): 
 
 
 
    i = self.pos[v] 
 
 
    self.array[i][1] = dist 
 
 
    while i > 0 and self.array[i][1] < self.array[(i - 1) // 2][1]: 
 
 
      self.pos[ self.array[i][0] ] = (i-1)//2
      self.pos[ self.array[(i-1)//2][0] ] = i 
      self.swapMinHeapNode(i, (i - 1)//2 ) 
 
      i = (i - 1) //2; 
 
 
  def isInMinHeap(self, v): 
 
    if self.pos[v] < self.size: 
      return True
    return False
 
 
'''def printArr(dist, n): 
  print("Vertex\tDistance from source")
  for i in range(n): 
    print("%d\t\t%d" % (i,dist[i]))'''
 
 
class Graph(): 
 
  def __init__(self, V): 
    self.V = V 
    self.graph = defaultdict(list) 
 
  def addEdge(self, src, dest, weight): 
 
 
    newNode = [dest, weight] 
    self.graph[src].insert(0, newNode) 
 
    newNode = [src, weight] 
    self.graph[dest].insert(0, newNode) 
 
  def printParent(self,parent,j):
      global pathSrcToDest
      if parent[j] == -1 :  
            pathSrcToDest.append(j)
            return
      self.printParent(parent , parent[j]) 
      pathSrcToDest.append(j)
        
  def dijkstra(self, src, dest,N,kVertices): 
    V = self.V 
    dist = []
    minHeap = Heap() 
    for v in range(V): 
      dist.append(10**30) 
      minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
      minHeap.pos.append(v) 
    minHeap.pos[src] = src 
    dist[src] = 0
    minHeap.decreaseKey(src, dist[src]) 
    minHeap.size = V;
    parent=[-1]*N
    pathlength=[0]*N
    Blackened=[0]*N
    Y=0
    while minHeap.isEmpty() == False: 
      newHeapNode = minHeap.extractMin() 
      u = newHeapNode[0]
      Blackened[u]=1
      if u not in kVertices:
          Y+=1
      for pCrawl in self.graph[u]: 
        v = pCrawl[0]
        if Blackened[v]==0 and minHeap.isInMinHeap(v) and dist[u] != 10**30 and (((pCrawl[1] + dist[u])*Y) < dist[v]):
            if v not in kVertices:
                Y+=1
            dist[v] = (pCrawl[1] + dist[u])*Y
            minHeap.decreaseKey(v, dist[v])
            parent[v]=u
            pathlength[v]= pathlength[parent[v]]+1
        elif Blackened[v]==0 and minHeap.isInMinHeap(v) and dist[u] != 10**30 and (((pCrawl[1] + dist[u])*Y) == dist[v]) and (pathlength[u]+1)<pathlength[v]:
            parent[v]= u
            pathlength[v] = pathlength[u] + 1
    if dist[dest]!=10**50:
        self.printParent(parent,dest)
 
def main():
    N,M,K = map(int,input().split())
    u,v=map(int,input().split())
    edgesDict={}
    g = Graph(N)
    for i in range(M):
        s,d,w=map(int,input().split())
        edgesDict[(min(s-1,d-1),max(s-1,d-1))]=i+1
        g.addEdge(s-1,d-1,w)
        
    kVertices={(x-1):0 for x in list(map(int,input().split()))}
    g.dijkstra(u-1,v-1,N,kVertices)
    edgesArr=[]
    for i in range(1,len(pathSrcToDest)):
        edgesArr.append((min(pathSrcToDest[i],pathSrcToDest[i-1]),max(pathSrcToDest[i],pathSrcToDest[i-1])))
    print(len(edgesArr))
    for edge in edgesArr:
        print(edgesDict[edge])
                  
if __name__=='__main__':
    main()
