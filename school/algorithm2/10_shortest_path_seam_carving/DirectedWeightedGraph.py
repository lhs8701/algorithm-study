from pathlib import Path
from queue import PriorityQueue
from queue import Queue
import timeit

class DirectedEdge:
    def __init__(self, v, w, weight): # Create an edge v->w with a double weight
        self.v, self.w, self.weight = v, w, weight
    
    def __lt__(self, other): # < operator, used to sort elements (e.g., in a PriorityQueue, sorted() function)
        assert(isinstance(other, DirectedEdge))
        return self.weight < other.weight

    def __gt__(self, other): # > operator, used to sort elements
        assert(isinstance(other, DirectedEdge))
        return self.weight > other.weight

    def __eq__(self, other): # == operator, used to compare edges for grading
        if other == None: return False
        assert(isinstance(other, DirectedEdge))
        return self.v == other.v and self.w == other.w and self.weight == other.weight

    def __str__(self): # Called when an Edge instance is printed (e.g., print(e))
        return f"{self.v}->{self.w} ({self.weight})"

    def __repr__(self): # Called when an Edge instance is printed as an element of a list
        return self.__str__()    


'''
Class for storing Weighted Digraphs
'''
class EdgeWeightedDigraph:
    def __init__(self, V): # Constructor
        self.V = V # Number of vertices
        self.E = 0 # Number of edges
        self.adj = [[] for _ in range(V)]   # adj[v] is a list of vertices adjacent to v
        self.edges = []

    def addEdge(self, v, w, weight): # Add edge v-w. Self-loops and parallel edges are allowed
        e = DirectedEdge(v, w, weight) # Create one edge instance and use it for adj[v], adj[w], and edges[]
        self.adj[v].append(e)        
        self.edges.append(e)
        self.E += 1
    
    def outDegree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for e in self.adj[v]: rtList.append(f"{e}\n")
        return "".join(rtList)

    def negate(self): # return an EdgeWeightedDigraph with all edge weights negated
        g = EdgeWeightedDigraph(self.V)
        for e in self.edges: g.addEdge(e.v, e.w, -e.weight)
        return g

    def reverse(self): # return an EdgeWeightedDigraph with all edges reversed
        g = EdgeWeightedDigraph(self.V)
        for e in self.edges: g.addEdge(e.w, e.v, e.weight)
        return g

    '''
    Create an EdgeWeightedDigraph from a file
        fileName: Name of the file that contains graph information as follows:
            (1) the number of vertices, followed by
            (2) one edge in each line, where an edge v->w with weight is represented by "v w weight"
            e.g., the following file represents a digraph with 3 vertices and 2 edges
            3
            0 1 0.12
            2 0 0.26
        The file needs to be in the same directory as the current .py file
    '''
    @staticmethod
    def fromFile(fileName):
        filePath = Path(__file__).with_name(fileName)   # Use the location of the current .py file   
        with filePath.open('r') as f:
            phase = 0
            line = f.readline().strip() # Read a line, while removing preceding and trailing whitespaces
            while line:                                
                if len(line) > 0:
                    if phase == 0: # Read V, the number of vertices
                        g = EdgeWeightedDigraph(int(line))
                        phase = 1
                    elif phase == 1: # Read edges
                        edge = line.split()
                        if len(edge) != 3: raise Exception(f"Invalid edge format found in {line}")
                        g.addEdge(int(edge[0]), int(edge[1]), float(edge[2]))                        
                line = f.readline().strip()
        return g


'''
Min Priority Queue based on a binary heap 
    with decreaseKey operation added
'''
class IndexMinPQ:
    def __init__(self, maxN): # Create an indexed PQ with indices 0 to (N-1)
        if maxN < 0: raise Exception("maxN < 0")
        self.maxN = maxN # Max number of elements on PQ
        self.n = 0 # Number of elements on PQ
        self.keys = [None] * (maxN+1)  # keys[i]: key with index i
        self.pq = [-1] * (maxN+1)  # pq[i]: index of the key at heap position i (pq[0] is not used)        
        self.qp = [-1] * maxN # qp[i]: heap position of the key with index i (inverse of pq[])        

    def isEmpty(self):
        return self.n == 0

    def contains(self, i): # Is i an index on the PQ?
        self.validateIndex(i)
        return self.qp[i] != -1

    def size(self):
        return self.n

    def insert(self, i, key): # Associate key with index i
        self.validateIndex(i)
        if self.contains(i): raise Exception(f"index {i} is already in PQ")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self.swimUp(self.n)

    def minIndex(self): # Index associated with the minimum key
        if self.n == 0: raise Exception("PQ has no element, so no min index exists")
        return self.pq[1]

    def minKey(self):
        if self.n == 0: raise Exception("PQ has no element, so no min key exists")
        return self.keys[self.pq[1]]

    def delMin(self):
        if self.n == 0: raise Exception("PQ has no element, so no element to delete")
        minIndex = self.pq[1]
        minKey = self.keys[minIndex]
        self.exch(1, self.n)
        self.n -= 1
        self.sink(1)
        assert(minIndex == self.pq[self.n+1])
        self.qp[minIndex] = -1 # Mark the index as being deleted
        self.keys[minIndex] = None
        self.pq[self.n+1] = -1
        return minKey, minIndex

    def keyOf(self, i):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        else: return self.keys[i]

    def changeKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        self.keys[i] = key
        self.swimUp(self.qp[i])
        self.sink(self.qp[i])

    def decreaseKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        if self.keys[i] == key: raise Exception(f"calling decreaseKey() with key {key} equal to the previous key")
        if self.keys[i] < key: raise Exception(f"calling decreaseKey() with key {key} greater than the previous key {self.keys[i]}")
        self.keys[i] = key
        self.swimUp(self.qp[i])

    def increaseKey(self, i, key):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        if self.keys[i] == key: raise Exception(f"calling increaseKey() with key {key} equal to the previous key")
        if self.keys[i] > key: raise Exception(f"calling increaseKey() with key {key} smaller than the previous key {self.keys[i]}")
        self.keys[i] = key
        self.sink(self.qp[i])

    def delete(self, i):
        self.validateIndex(i)
        if not self.contains(i): raise Exception(f"index {i} is not in PQ")
        idx = self.qp[i]
        self.exch(idx, self.n)
        self.n -= 1
        self.swimUp(idx)
        self.sink(idx)
        self.keys[i] = None
        self.qp[i] = -1   

    def validateIndex(self, i):
        if i < 0: raise Exception(f"index {i} < 0")
        if i >= self.maxN: raise Exception(f"index {i} >= capacity {self.maxN}")

    def greater(self, i, j):
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def exch(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def swimUp(self, idx): # idx is the index in pq[]
        while idx>1 and self.greater(idx//2, idx):
            self.exch(idx, idx//2)            
            idx = idx//2

    def sink(self, idx): # idx is the index in pq[]
        while 2*idx <= self.n:    # If a child exists
            idxChild = 2*idx # Left child
            if idxChild<self.n and self.greater(idxChild, idxChild+1): idxChild = idxChild+1 # Find the smaller child
            if not self.greater(idx, idxChild): break
            self.exch(idx, idxChild) # Swap with (i.e., sink to) the greater child
            idx = idxChild


'''
Perform the topological sort on a DAG g, while detecing any cycle
    If a cycle is found, return False
    Otherwise, return list of vertices in reverse DFS postorder
'''
def topologicalSortWithCycleDetection(g):
    def recur(v):        
        visited[v] = True
        verticesInRecurStack.add(v)
        for e in g.adj[v]:
            if e.w in verticesInRecurStack: # Edge found to a vertex in the recursive stack
                print("cycle detected on vertex", e.w)                
                return False 
            if not visited[e.w]: 
                if not recur(e.w): return False
        reverseList.append(v) # Add v to the stack if all adjacent vertices were visited
        verticesInRecurStack.remove(v)
        return True

    assert(isinstance(g, EdgeWeightedDigraph))
    visited = [False for _ in range(g.V)]
    reverseList = []
    verticesInRecurStack = set() # Initialize set before the first call of recur()
    for v in range(g.V): 
        if not visited[v]:
            #verticesInRecurStack = set() # Initialize set before the first call of recur()
            if not recur(v): # Return False if a cycle is detected                
                return None

    reverseList.reverse()
    return reverseList


'''
Class that finds and stores shortest paths from a single source    
'''
class SP:
    def __init__(self, g, s): # Find shortest paths from s in graph g
        if not isinstance(g, EdgeWeightedDigraph): raise Exception(f"{g} is not an EdgeWeightedDigraph")
        self.g, self.s = g, s
        self.validateVertex(s)        
        self.edgeTo = [None] * g.V # edgeTo[w]: last edge on the shortest known path to w
        self.distTo = [float('inf')] * g.V  # distTo[w]: shortest known distance to w
        self.distTo[s] = 0

    def pathTo(self, v):
        self.validateVertex(v)
        if not self.hasPathTo(v): raise Exception(f"no path exists to vertex {v}")
        path = []
        e = self.edgeTo[v]
        while e != None:
            path.append(e)
            e = self.edgeTo[e.v]
        path.reverse()
        return path

    def hasPathTo(self, v):
        self.validateVertex(v)
        return self.distTo[v] < float('inf')

    # If e=v->w gives a shorter path to w through v
    #   update distTo[w] and edgeTo[w]
    def relax(self, e):
        assert(isinstance(e, DirectedEdge))        
        if self.distTo[e.w] > self.distTo[e.v] +  e.weight:
            self.distTo[e.w] = self.distTo[e.v] +  e.weight
            self.edgeTo[e.w] = e

    def validateVertex(self, v):
        if v<0 or v>=self.g.V: raise Exception(f"vertex {v} is not between 0 and {self.g.V-1}")


class DijkstraSP(SP): # Inherit SP class
    def __init__(self, g, s):
        super().__init__(g, s) # run the constructor of the parent class
        self.pq = IndexMinPQ(g.V)
        self.pq.insert(s, 0) # insert (source vertex id, distance)
        self.closed = [False] * g.V
        while not self.pq.isEmpty():
            # select vertices in order of distance from s
            dist, v = self.pq.delMin()
            self.closed[v] = True            
            for e in self.g.adj[v]:
                if not self.closed[e.w]: self.relax(e)

    def relax(self, e):
        assert(isinstance(e, DirectedEdge))        
        if self.distTo[e.w] > self.distTo[e.v] +  e.weight:
            self.distTo[e.w] = self.distTo[e.v] +  e.weight
            self.edgeTo[e.w] = e
            if self.pq.contains(e.w): self.pq.decreaseKey(e.w, self.distTo[e.w])
            else: self.pq.insert(e.w, self.distTo[e.w])


class AcyclicSP(SP):
    def __init__(self, g, s):
        super().__init__(g, s) # run the constructor of the parent class
        tpOrder = topologicalSortWithCycleDetection(g)
        assert(tpOrder != None) # confirm no cycle
        for v in tpOrder:
           for e in self.g.adj[v]:
                self.relax(e) 


class BellmanFordSP(SP):
    def __init__(self, g, s):
        super().__init__(g, s)
        self.q = Queue(maxsize=g.V)
        self.onQ = [False] * g.V
        self.q.put(s)        
        self.onQ[s] = True
        while self.q.qsize() > 0:        
            v = self.q.get()
            self.onQ[v] = False
            for e in self.g.adj[v]:
                self.relax(e)

    def relax(self, e):
        assert(isinstance(e, DirectedEdge))        
        if self.distTo[e.w] > self.distTo[e.v] +  e.weight:
            self.distTo[e.w] = self.distTo[e.v] +  e.weight
            self.edgeTo[e.w] = e
            if not self.onQ[e.w]:
                self.q.put(e.w)
                self.onQ[e.w] = True


if __name__ == "__main__":
    e1 = DirectedEdge(2,3,0.1)
    e1a = DirectedEdge(2,3,0.1)
    e2 = DirectedEdge(3,4,0.9)
    e3 = DirectedEdge(7,3,0.2)
    print("e1, e1a, e2, e3", e1, e1a, e2, e3)
    print("e1 == e1a", e1 == e1a)
    print("e1 < e2", e1 < e2)
    print("e1 > e3", e1 > e3)
    print("e2 < e3", e2 < e3)

    g1 = EdgeWeightedDigraph(8)
    g1.addEdge(4,5,0.35)
    g1.addEdge(5,4,0.35)
    g1.addEdge(4,7,0.37)
    g1.addEdge(5,7,0.28)
    g1.addEdge(7,5,0.28)
    g1.addEdge(5,1,0.32)
    g1.addEdge(0,4,0.38)
    g1.addEdge(0,2,0.26)
    g1.addEdge(7,3,0.39)
    g1.addEdge(1,3,0.29)
    g1.addEdge(2,7,0.34)
    g1.addEdge(6,2,0.40)
    g1.addEdge(3,6,0.52)
    g1.addEdge(6,0,0.58)
    g1.addEdge(6,4,0.93)
    print(g1)
    print(g1.adj[0])       
    print(g1.adj[7])
    print()

    g8i = EdgeWeightedDigraph.fromFile("wdigraph8i.txt")
    print("g8i", g8i)
    print("dijkstraSP on g8i")
    sp8i = DijkstraSP(g8i, 0)
    for i in range(g8i.V):
        if sp8i.hasPathTo(i): print(i, sp8i.distTo[i], sp8i.pathTo(i))
        else: print(i, "no path exists")
    print()

    g8a = EdgeWeightedDigraph.fromFile("wdigraph8a.txt")    
    print("g8a", g8a)
    print("dijkstraSP on g8a")
    sp8a = DijkstraSP(g8a, 0)
    print(sp8a.distTo)
    print(sp8a.edgeTo)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    print("BellmanFordSP on g8a")
    sp8a = BellmanFordSP(g8a, 0)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    print("acyclicSP on g8a")
    sp8a = AcyclicSP(g8a, 4)
    print(sp8a.distTo)
    print(sp8a.edgeTo)
    for i in range(g8a.V):
        if sp8a.hasPathTo(i): print(i, sp8a.distTo[i], sp8a.pathTo(i))
        else: print(i, "no path exists")
    print()

    g8bn = EdgeWeightedDigraph.fromFile("wdigraph8b.txt").negate()
    print("acyclicSP on -g8b for vertex 5 as the source to find longest paths")
    sp8bn = AcyclicSP(g8bn, 5)
    for i in range(g8bn.V):
        if sp8bn.hasPathTo(i): print(i, -sp8bn.distTo[i], sp8bn.pathTo(i))
        else: print(i, "no path exists")    
    print()
    
    g6n = EdgeWeightedDigraph.fromFile("wdigraph6n.txt")
    print("BellmanFordSP on g6n")
    sp6n = BellmanFordSP(g6n, 0)
    for i in range(g6n.V):
        if sp6n.hasPathTo(i): print(i, sp6n.distTo[i], sp6n.pathTo(i))
        else: print(i, "no path exists")    
    print()

    print("DijkstraSP on g6n")
    sp6nD = DijkstraSP(g6n, 0)
    for i in range(g6n.V):
        if sp6nD.hasPathTo(i): print(i, sp6nD.distTo[i], sp6nD.pathTo(i))
        else: print(i, "no path exists")    
    print()
