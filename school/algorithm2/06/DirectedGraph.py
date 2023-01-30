import requests  # For reading web pages
import re  # For searching with regular expressions
import timeit
from queue import Queue

'''
Class for storing directed graphs
'''


class Digraph:
    def __init__(self, V):  # Constructor
        self.V = V  # Number of vertices
        self.E = 0  # Number of edges
        self.adj = [[] for _ in range(V)]  # adj[v] is a list of vertices pointed from v

    def addEdge(self, v, w):  # Add a directed edge v->w. Self-loops and parallel edges are allowed
        self.adj[v].append(w)
        self.E += 1

    def outDegree(self, v):
        return len(self.adj[v])

    def __str__(self):
        rtList = [f"{self.V} vertices and {self.E} edges\n"]
        for v in range(self.V):
            for w in self.adj[v]:
                rtList.append(f"{v}->{w}\n")
        return "".join(rtList)

    def reverse(self):  # return a digraph with all edges reversed
        g = Digraph(self.V)
        for v in range(self.V):
            for w in self.adj[v]: g.addEdge(w, v)
        return g


'''
Class for storing the results of depth-first search
'''


class DFS:
    # Constructor
    # Perform DFS on graph g starting from the source vertex s
    def __init__(self, g, s):
        def recur(v):
            self.visited[v] = True
            for w in g.mat[v]:
                if not self.visited[w]:
                    recur(w)
                    self.fromVertex[w] = v

        assert (isinstance(g, Digraph) and s >= 0 and s < g.V)
        self.g, self.s = g, s
        self.visited = [False for _ in range(g.V)]
        self.fromVertex = [None for _ in range(g.V)]
        recur(s)

        # Return a list of vertices on the path from s to v

    #     based on the results of DFS
    def pathTo(self, v):
        if not self.visited[v]: return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.fromVertex[v]
        path.append(self.s)
        path.reverse()
        return path

    def hasPathTo(self, v):
        return self.visited[v]


# This function is used to evaluate the speed of SCC class
# 
def DFSforEvaluation(g):
    def recur(v):
        visited[v] = True
        for w in g.mat[v]:
            if not visited[w]:
                recur(w)
                fromVertex[w] = v

    assert (isinstance(g, Digraph))
    visited = [False for _ in range(g.V)]
    fromVertex = [None for _ in range(g.V)]
    for v in range(g.V):
        if not visited[v]:
            recur(v)

    return visited, fromVertex


'''
Class for storing the results of breadth-first search
'''


class BFS:
    # Constructor
    # PerformBDFS on graph g starting from the source vertex s
    def __init__(self, g, s):
        assert (isinstance(g, Digraph) and s >= 0 and s < g.V)
        self.g, self.s = g, s
        self.visited = [False for _ in range(g.V)]
        self.fromVertex = [None for _ in range(g.V)]
        self.distance = [None for _ in range(g.V)]
        queue = Queue()
        queue.put(s)
        self.visited[s] = True
        self.distance[s] = 0
        while queue.qsize() > 0:
            v = queue.get()
            for w in g.adj[v]:
                if not self.visited[w]:
                    queue.put(w)
                    self.visited[w] = True
                    self.fromVertex[w] = v
                    self.distance[w] = self.distance[v] + 1

    # Return a list of vertices on the path from s to v
    #     based on the results of DFS
    def pathTo(self, v):
        if not self.visited[v]: return None
        path = []
        while v != self.s:
            path.append(v)
            v = self.fromVertex[v]
        path.append(self.s)
        path.reverse()
        return path

    def hasPathTo(self, v):
        return self.visited[v]

    def distTo(self, v):
        return self.distance[v]


'''
Discover web addresses through BFS, starting from root addresses as the source set
    roots: list of web addresses to use as the source set
'''
webaddrPattern = re.compile(
    "https://(?:\\w+\\.)+(?:\\w+)")  # Regex pattern for a web address. '?:' indicates a non-capturing group


def webCrawl(roots, maxDepth=1):
    queue = Queue()
    discovered = {}  # Symbol table of discovered sites and depth, where depth is the distance from sources
    for v in roots:
        queue.put(v)
        discovered[v] = 0

    while queue.qsize() > 0:
        v = queue.get()
        depth = discovered[v]
        if depth > maxDepth: break

        try:
            resp = requests.get(v)  # Receive response by visiting the web site at v
            if resp.status_code == 200:  # HTTP status code '200 OK' means the page was successfully retrieved
                print(v, f"(depth={depth})")
                for w in webaddrPattern.findall(resp.text):
                    if w not in discovered:
                        discovered[w] = depth + 1
                        queue.put(w)
        except requests.exceptions.ConnectionError as error:
            pass


'''
Perform the topological sort on a DAG g, and return list of vertices in reverse DFS postorder
'''


def topologicalSort(g):
    def recur(v):
        visited[v] = True
        for w in g.mat[v]:
            if not visited[w]: recur(w)
        reverseList.append(v)  # Add v to the stack if all adjacent vertices were visited

    assert (isinstance(g, Digraph))
    visited = [False for _ in range(g.V)]
    reverseList = []
    for v in range(g.V):
        if not visited[v]: recur(v)

    reverseList.reverse()
    return reverseList


'''
Class that finds SCC (Strongly-Connected Components) and stores the results    
'''


class SCC:
    def __init__(self, g):  # Do strongly-connected-components pre-processing, based on Kosaraju-Sharir algorithm
        def recur(v):  # DFS to mark all vertices connected to v
            self.id[v] = self.count
            for w in g.mat[v]:
                if self.id[w] < 0:
                    recur(w)

        self.g = g
        self.id = [-1 for i in range(g.V)]  # id[v] is the ID of component to which v belongs (-1 for not visited)
        self.count = 0  # Number of connected components
        temp = g.reverse()
        arr = topologicalSort(temp)
        for v in arr:
            if self.id[v] < 0:
                recur(v)
                self.count += 1

    def connected(self, v, w):  # Are v and w connected?
        return self.id[v] == self.id[w]


if __name__ == "__main__":
    '''# Unit test for Digraph
    g = Digraph(13)
    g.addEdge(0,1)
    g.addEdge(0,5)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,2)
    g.addEdge(3,5)
    g.addEdge(4,2)
    g.addEdge(4,3)
    g.addEdge(5,4)
    g.addEdge(6,0)
    g.addEdge(6,4)
    g.addEdge(6,8)
    g.addEdge(6,9)
    g.addEdge(7,6)
    g.addEdge(7,9)
    g.addEdge(8,6)
    g.addEdge(9,10)
    g.addEdge(9,11)
    g.addEdge(10,12)
    g.addEdge(11,4)
    g.addEdge(11,12)
    g.addEdge(12,9)
    print(g)    
    print(g.adj[0], g.outDegree(0))    
    print(g.adj[5], g.outDegree(5))
    print(g.adj[9], g.outDegree(9))
    
    gr = g.reverse()
    print(gr)
    print(gr.adj[0], gr.outDegree(0))    
    print(gr.adj[5], gr.outDegree(5))
    print(gr.adj[9], gr.outDegree(9))
    
    dfs = DFS(g,0)
    print(dfs.visited, dfs.fromVertex)
    print(dfs.pathTo(0))
    print(dfs.pathTo(1))
    print(dfs.pathTo(2))
    print(dfs.pathTo(3))
    print(dfs.pathTo(4))
    print(dfs.pathTo(5))
    print(dfs.pathTo(6))
    print(dfs.pathTo(7))
    print(dfs.hasPathTo(6))
    print(dfs.hasPathTo(7))
    
    bfs = BFS(g,0)
    print(bfs.visited, bfs.fromVertex)
    print(bfs.pathTo(0), bfs.distTo(0))
    print(bfs.pathTo(1), bfs.distTo(1))
    print(bfs.pathTo(2), bfs.distTo(2))
    print(bfs.pathTo(3), bfs.distTo(3))
    print(bfs.pathTo(4), bfs.distTo(4))
    print(bfs.pathTo(5), bfs.distTo(5))
    print(bfs.pathTo(6), bfs.distTo(6))
    print(bfs.pathTo(7), bfs.distTo(7))
    print(dfs.hasPathTo(6))
    print(dfs.hasPathTo(7))'''

    '''# Unit test for Web crawling
    #resp = requests.get("https://www.naver.com/")
    #print(resp.text)
    webCrawl(["https://www.naver.com/", "https://www.daum.net/"])'''

    '''# Unit test for topological Sort
    tasks = Digraph(7)        
    tasks.addEdge(0,1)
    tasks.addEdge(0,2)
    tasks.addEdge(0,5)
    tasks.addEdge(1,4)    
    tasks.addEdge(3,2)
    tasks.addEdge(3,4)
    tasks.addEdge(3,5)
    tasks.addEdge(3,6)
    tasks.addEdge(5,2)
    tasks.addEdge(6,0)   
    tasks.addEdge(6,4)    
    print(topologicalSort(tasks))
    
    g5 = Digraph(5)
    g5.addEdge(0,1)
    g5.addEdge(1,3)
    g5.addEdge(1,2)
    g5.addEdge(2,3)
    g5.addEdge(3,4)
    g5.addEdge(2,4)
    print("g5, topological order", topologicalSort(g5))
    print("g5r, topological order", topologicalSort(g5.reverse()))'''

    # Unit test for Kosaraju-Sharir for Finding Strongly-Connected Components
    g1 = Digraph(6)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 4)
    g1.addEdge(3, 5)
    g1.addEdge(4, 0)
    g1.addEdge(4, 1)
    g1.addEdge(5, 3)
    g1.addEdge(5, 4)
    scc1 = SCC(g1)
    print("scc1.count, scc1.id", scc1.count, scc1.id)
    if scc1.count == 2:
        print("pass")
    else:
        print("fail")
    if all([idx >= 0 and idx < scc1.count for idx in scc1.id]):
        print("pass")
    else:
        print("fail")
    print("scc1.connected(1,4)", scc1.connected(1, 4))
    if scc1.connected(1, 4):
        print("pass")
    else:
        print("fail")
    print("scc1.connected(2,5)", scc1.connected(2, 5))
    if not scc1.connected(2, 5):
        print("pass")
    else:
        print("fail")
    print("scc1.connected(3,5)", scc1.connected(3, 5))
    if scc1.connected(3, 5):
        print("pass")
    else:
        print("fail")
    print()

    g2 = Digraph(7)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(1, 3)
    g2.addEdge(2, 3)
    g2.addEdge(2, 4)
    g2.addEdge(3, 4)
    g2.addEdge(5, 6)
    g2.addEdge(6, 2)
    g2.addEdge(6, 5)
    scc2 = SCC(g2)
    print("scc2.count, scc2.id", scc2.count, scc2.id)
    print("scc2.connected(0,2)", scc2.connected(0, 2))
    print("scc2.connected(2,4)", scc2.connected(2, 4))
    print("scc2.connected(4,5)", scc2.connected(4, 5))
    print("scc2.connected(5,6)", scc2.connected(5, 6))
    print()

    g3 = Digraph(13)
    g3.addEdge(0, 1)
    g3.addEdge(0, 5)
    g3.addEdge(2, 0)
    g3.addEdge(2, 3)
    g3.addEdge(3, 2)
    g3.addEdge(3, 5)
    g3.addEdge(4, 2)
    g3.addEdge(4, 3)
    g3.addEdge(5, 4)
    g3.addEdge(6, 0)
    g3.addEdge(6, 4)
    g3.addEdge(6, 8)
    g3.addEdge(6, 9)
    g3.addEdge(7, 6)
    g3.addEdge(7, 9)
    g3.addEdge(8, 6)
    g3.addEdge(9, 10)
    g3.addEdge(9, 11)
    g3.addEdge(10, 12)
    g3.addEdge(11, 4)
    g3.addEdge(11, 12)
    g3.addEdge(12, 9)
    print("topologicalSort(g3.reverse())", topologicalSort(g3.reverse()))
    print("topologicalSort(g3)", topologicalSort(g3))

    scc3 = SCC(g3)
    print("scc3.count, scc3.id", scc3.count, scc3.id)
    print("scc3.connected(0,3)", scc3.connected(0, 3))
    print("scc3.connected(0,7)", scc3.connected(0, 7))
    print("scc3.connected(0,9)", scc3.connected(0, 9))
    print("scc3.connected(7,8)", scc3.connected(7, 8))
    print("scc3.connected(7,11)", scc3.connected(7, 11))
    print("scc3.connected(10,12)", scc3.connected(10, 12))
    print()

    '''# Unit test for speed
    n=10000
    tSCC = timeit.timeit(lambda: scc3.connected(4,5), number=n)/n    
    tDFS = timeit.timeit(lambda: DFSforEvaluation(g3), number=n)/n    
    print(f"{n} calls of connected() on g3 took {tSCC:.10f} sec on average, and the same number of calls of DFS() took {tDFS:.10f} sec on average")
    if tSCC*10 < tDFS: print("pass")
    else: print("fail")'''
