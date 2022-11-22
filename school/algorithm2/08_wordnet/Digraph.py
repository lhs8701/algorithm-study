from pathlib import Path
from queue import Queue
import math  # To use infinity in sap()
import timeit

'''
Class for storing directed graphs
'''


class Digraph:
    def __init__(self, V):  # Constructor
        self.V = V  # Number of vertices
        self.E = 0  # Number of edges
        self.adj = [[] for _ in range(V)]  # adj[v] is a list of vertices pointed from v

    def addEdge(self, v, w):  # Add a directed edge v->w. Self-loops and parallel edges are allowed
        if v < 0 or v >= self.V: raise Exception(f"Vertex id {v} is not within the range [{0}-{(self.V - 1)}]")
        if w < 0 or w >= self.V: raise Exception(f"Vertex id {w} is not within the range [{0}-{(self.V - 1)}]")
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
    Create a Digraph instance from a file
        fileName: Name of the file that contains graph information as follows:
            (1) the number of vertices, followed by
            (2) one edge in each line, where an edge v-w is represented by "v w"
            e.g., the following file represents a digraph with 2 vertices {0,1} and 2 edges {0-1, 1-0}
            2
            0 1
            1 0
        The file needs to be in the same directory as the current .py file
    '''

    @staticmethod
    def digraphFromFile(fileName):
        filePath = Path(__file__).with_name(fileName)  # Use the location of the current .py file
        with filePath.open('r') as f:
            phase = 0
            line = f.readline().strip()  # Read a line, while removing preceding and trailing whitespaces
            while line:
                if len(line) > 0:
                    if phase == 0:  # Read V, the number of vertices
                        g = Digraph(int(line))
                        phase = 1
                    elif phase == 1:  # Read edges
                        vw = line.split()
                        if len(vw) != 2: raise Exception(f"Invalid edge format found in {line}")
                        g.addEdge(int(vw[0]), int(vw[1]))
                line = f.readline().strip()
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
            for w in g.adj[v]:
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


# This function is used to evaluate the speed of sap() function
def BFSforEvaluation(g):
    def bfs(s):
        queue = Queue()
        queue.put(s)
        visited[s] = True
        distance[s] = 0
        while queue.qsize() > 0:
            v = queue.get()
            for w in g.adj[v]:
                if not visited[w]:
                    queue.put(w)
                    visited[w] = True
                    fromVertex[w] = v
                    distance[w] = distance[v] + 1

    visited = [False for _ in range(g.V)]
    fromVertex = [None for _ in range(g.V)]
    distance = [None for _ in range(g.V)]
    for v in range(g.V):
        if not visited[v]: bfs(v)


'''
Perform the topological sort on a DAG g, and return list of vertices in reverse DFS postorder
'''


def topologicalSort(g):
    def recur(v):
        visited[v] = True
        for w in g.adj[v]:
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
Perform the topological sort on a DAG g, while detecing any cycle
    If a cycle is found, return False
    Otherwise, return list of vertices in reverse DFS postorder
'''


def topologicalSortWithCycleDetection(g):
    def recur(v):
        visited[v] = True
        verticesInRecurStack.add(v)
        for w in g.adj[v]:
            if w in verticesInRecurStack:  # Edge found to a vertex in the recursive stack
                print("cycle detected on vertex", w)
                return True
            if not visited[w]:
                if recur(w): return True
        reverseList.append(v)  # Add v to the stack if all adjacent vertices were visited
        verticesInRecurStack.remove(v)
        return False

    assert (isinstance(g, Digraph))
    visited = [False for _ in range(g.V)]
    reverseList = []
    verticesInRecurStack = set()  # Initialize set before the first call of recur()
    for v in range(g.V):
        if not visited[v]:
            # verticesInRecurStack = set() # Initialize set before the first call of recur()
            if recur(v):  # Return None if a cycle is detected
                return None

    reverseList.reverse()
    return reverseList


def cycleDetection(g):
    def recur(v):
        visited[v] = True
        verticesInRecurStack.add(v)
        for w in g.adj[v]:
            if w in verticesInRecurStack:  # Edge found to a vertex in the recursive stack
                # print("cycle detected on vertex", w)
                return True
            if not visited[w]:
                if recur(w): return True
        verticesInRecurStack.remove(v)
        return False

    assert (isinstance(g, Digraph))
    visited = [False for _ in range(g.V)]
    verticesInRecurStack = set()  # Initialize set before the first call of recur()
    for v in range(g.V):
        if not visited[v]:
            if recur(v): return True
    return False


'''
Find the sap(shortest ancestral path) on digraph g between any vertex in aList and any vertex in bList
Return the common ancestor and the length of sap
'''


def sap(g, aList, bList):
    # Q 초기화 (aList와 bList객체 모두 put)
    # 3-tuple : (정점번호, aList/bList 중 어디서 왔는지(aList->0 / bList->1), 거쳐온거리)
    visited = [[-1, -1] for _ in range(g.V)]
    sapLength = math.inf
    Q = Queue()
    sca = -1
    flag = False
    for a in aList:
        Q.put((a, 0, 0))
        visited[a][0] = 0
        if a in bList:
            flag = True
            sca = a
            break

    # aList와 bList 모두에 속하는 정점번호 v가 있는지 확인 (있다면 (v, 0)을 바로 리턴 후 종료)
    if flag:
        return sca, 0

    for b in bList:
        Q.put((b, 1, 0))
        visited[b][1] = 0

    while not Q.empty():
        v = Q.get()
        if v[2] > sapLength:
            break
        for w in g.adj[v[0]]:  # v -> w 간선있는 각 정점 w에 대해
            if v[1] == 0:
                if visited[w][0] == -1:
                    Q.put((w, 0, v[2] + 1))
                    visited[w][0] = v[2] + 1

                if visited[w][1] != -1:
                    if sapLength > visited[w][0] + visited[w][1]:
                        sca = w
                        sapLength = visited[w][0] + visited[w][1]

            else:
                if visited[w][1] == -1:
                    Q.put((w, 1, v[2] + 1))
                    visited[w][1] = v[2] + 1

                if visited[w][0] != -1:
                    if sapLength > visited[w][0] + visited[w][1]:
                        sca = w
                        sapLength = visited[w][0] + visited[w][1]
    return sca, sapLength


class WordNet:
    def __init__(self, synsetFileName, hypernymFileName):  # Constructor
        self.synsets = []
        self.nounToIndex = {}  # (noun, list of indices in self.synsets)

        # Create vertices        
        synsetFilePath = Path(__file__).with_name(synsetFileName)  # Use the location of the current .py file
        with synsetFilePath.open('r') as f:
            line = f.readline().strip()  # Read a line, while removing preceding and trailing whitespaces
            while line:
                if len(line) > 0:
                    tokens = line.split(',')
                    self.synsets.append(tokens[1])
                    for word in tokens[1].split():
                        if word not in self.nounToIndex: self.nounToIndex[word] = []
                        self.nounToIndex[word].append(int(tokens[0]))
                line = f.readline().strip()
        self.g = Digraph(len(self.synsets))

        # Create edges        
        hypernymFilePath = Path(__file__).with_name(hypernymFileName)  # Use the location of the current .py file
        with hypernymFilePath.open('r') as f:
            line = f.readline().strip()  # Read a line, while removing preceding and trailing whitespaces
            while line:
                if len(line) > 0:
                    tokens = line.split(',')
                    v = int(tokens[0])
                    for idx in range(1, len(tokens)):
                        self.g.addEdge(v, int(tokens[idx]))
                line = f.readline().strip()

        # Check to see if the graph is a rooted DAG
        numVerticesWithZeroOutdegree = 0
        for v in range(self.g.V):
            if self.g.outDegree(v) == 0:
                numVerticesWithZeroOutdegree += 1
                # print("vertex with 0 outdegree", self.synsets[v])
        if numVerticesWithZeroOutdegree != 1: raise Exception(
            f"The graph has {numVerticesWithZeroOutdegree} vertices with outdegree=0")

        if cycleDetection(self.g): raise Exception("The graph contains a cycle")

    def nouns(self):  # Return all WordNet nouns (for debugging)
        return self.nounToIndex.keys()

    def isNoun(self, word):  # Is word a WordNet noun?
        return word in self.nounToIndex

    # Return the shortest common ancestor of nounA and nounB and the distance
    #   in a shortest ancestral path
    def sap(self, nounA, nounB):
        if nounA not in self.nounToIndex: raise Exception(f"{nounA} not in WordNet")
        if nounB not in self.nounToIndex: raise Exception(f"{nounB} not in WordNet")
        sca, distance = sap(self.g, self.nounToIndex[nounA], self.nounToIndex[nounB])
        return self.synsets[sca], distance


def outcast(wordNet, wordFileName):
    words = set()
    filePath = Path(__file__).with_name(wordFileName)  # Use the location of the current .py file
    with filePath.open('r') as f:
        line = f.readline().strip()  # Read a line, while removing preceding and trailing whitespaces
        while line:
            if len(line) > 0:
                words.update(line.split())
            line = f.readline().strip()

    maxDistance = -1
    maxDistanceWord = None
    for nounA in words:
        distanceSum = 0
        for nounB in words:
            if nounA != nounB:
                _, distance = wordNet.sap(nounA, nounB)
                distanceSum += distance
        if distanceSum > maxDistance:
            maxDistance = distanceSum
            maxDistanceWord = nounA

    return maxDistanceWord, maxDistance, words


if __name__ == "__main__":
    '''# Unit test for topological sort and cycle detection
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
    
    print(topologicalSortWithCycleDetection(tasks)) # No cycle detected
    print(cycleDetection(tasks))
    
    tasks.addEdge(2,3)
    print(topologicalSortWithCycleDetection(tasks)) # cycle detected
    print(cycleDetection(tasks))

    d5 = Digraph(5)
    d5.addEdge(0,1)
    d5.addEdge(1,3)
    d5.addEdge(3,2)
    d5.addEdge(3,4)
    d5.addEdge(4,1)
    print(cycleDetection(d5))'''

    # Unit test for sap()
    print('digraph6.txt')
    d6 = Digraph.digraphFromFile('digraph6.txt')

    print(sap(d6, [1], [5]))
    if sap(d6, [1], [5]) == (0, 2):
        print("pass")
    else:
        print("fail")

    print(sap(d6, [1], [1]))
    if sap(d6, [1], [1]) == (1, 0):
        print("pass")
    else:
        print("fail")

    print(sap(d6, [1], [4]))  # Either (0,3) or (4,3)
    tmp = sap(d6, [1], [4])
    if tmp == (0, 3) or tmp == (4, 3):
        print("pass")
    else:
        print("fail")
    # ----------------------------------------------------------------------
    print(sap(d6, [1], [3]))
    if sap(d6, [1], [3]) == (3, 2):
        print("pass")
    else:
        print("fail")

    print('digraph12.txt')
    d12 = Digraph.digraphFromFile('digraph12.txt')
    print(sap(d12, [3], [10]))  # (1,4)
    if sap(d12, [3], [10]) == (1, 4):
        print("pass")
    else:
        print("fail")
    print(sap(d12, [3], [10, 2]))  # (0,3)
    if sap(d12, [3], [10, 2]) == (0, 3):
        print("pass")
    else:
        print("fail")

    print('digraph25.txt')
    d25 = Digraph.digraphFromFile('digraph25.txt')
    print(sap(d25, [13, 23, 24], [6, 16, 17]))  # (3,4)
    if sap(d25, [13, 23, 24], [6, 16, 17]) == (3, 4):
        print("pass")
    else:
        print("fail")
    print(sap(d25, [13, 23, 24], [6, 16, 17, 4]))  # (3,4) or (1,4)
    tmp = sap(d25, [13, 23, 24], [6, 16, 17, 4])
    if tmp == (3, 4) or tmp == (1, 4):
        print("pass")
    else:
        print("fail")
    print(sap(d25, [13, 23, 24], [6, 16, 17, 1]))  # (1,3)
    if sap(d25, [13, 23, 24], [6, 16, 17, 1]) == (1, 3):
        print("pass")
    else:
        print("fail")
    print(sap(d25, [13, 23, 24, 17], [6, 16, 17, 1]))  # (17,0)
    if sap(d25, [13, 23, 24, 17], [6, 16, 17, 1]) == (17, 0):
        print("pass")
    else:
        print("fail")

    # Unit test with WordNet
    print('WordNet test')
    wn = WordNet("synsets.txt", "hypernyms.txt")
    print(wn.isNoun("blue"))
    print(wn.isNoun("fox"))
    print(wn.isNoun("lalala"))
    print(wn.sap("blue", "red"))
    tmp = wn.sap("blue", "red")
    if tmp != None and len(tmp) == 2 and tmp[1] == 2:
        print("pass")
    else:
        print("fail")
    print(wn.sap("blue", "fox"))
    tmp = wn.sap("blue", "fox")
    if tmp != None and len(tmp) == 2 and tmp[1] == 8:
        print("pass")
    else:
        print("fail")
    print(wn.sap("apple", "banana"))
    tmp = wn.sap("apple", "banana")
    if tmp != None and len(tmp) == 2 and tmp[1] == 2:
        print("pass")
    else:
        print("fail")
    print(wn.sap("George_W._Bush", "JFK"))
    tmp = wn.sap("George_W._Bush", "JFK")
    if tmp != None and len(tmp) == 2 and tmp[1] == 2:
        print("pass")
    else:
        print("fail")
    print(wn.sap("George_W._Bush", "Eric_Arthur_Blair"))
    tmp = wn.sap("George_W._Bush", "Eric_Arthur_Blair")
    if tmp != None and len(tmp) == 2 and tmp[1] == 7:
        print("pass")
    else:
        print("fail")
    print(wn.sap("George_W._Bush", "chimpanzee"))
    tmp = wn.sap("George_W._Bush", "chimpanzee")
    if tmp != None and len(tmp) == 2 and tmp[1] == 17:
        print("pass")
    else:
        print("fail")

    print('outcast test')
    print(outcast(wn, "outcast5.txt"))
    tmp = outcast(wn, "outcast5.txt")
    if tmp != None and len(tmp) == 3 and tmp[0] == "table":
        print("pass")
    else:
        print("fail")
    print(outcast(wn, "outcast8.txt"))
    tmp = outcast(wn, "outcast8.txt")
    if tmp != None and len(tmp) == 3 and tmp[0] == "bed":
        print("pass")
    else:
        print("fail")
    print(outcast(wn, "outcast11.txt"))
    tmp = outcast(wn, "outcast11.txt")
    if tmp != None and len(tmp) == 3 and tmp[0] == "potato":
        print("pass")
    else:
        print("fail")
    print(outcast(wn, "outcast9.txt"))
    tmp = outcast(wn, "outcast9.txt")
    if tmp != None and len(tmp) == 3 and tmp[0] == "fox":
        print("pass")
    else:
        print("fail")
    ''''''
    # Unit test for speed
    print('speed test')
    n = 1000
    d25 = Digraph.digraphFromFile('digraph25.txt')
    tSAP = timeit.timeit(lambda: sap(d25, [13, 23, 24], [6, 16, 17]), number=n) / n
    tBFS = timeit.timeit(lambda: BFSforEvaluation(d25), number=n) / n
    print(
        f"{n} calls of sap() on d25 took {tSAP:.10f} sec on average, and the same number of calls of BFS() took {tBFS:.10f} sec on average")
    if tSAP < tBFS:
        print("pass")
    else:
        print("fail")
    ''''''
