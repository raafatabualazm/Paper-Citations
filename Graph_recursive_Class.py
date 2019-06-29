from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.graphIn = defaultdict(set)
        self.communities = defaultdict(set)

    def addEdge(self, u, v):
        self.graph[u].add(v)
        self.graphIn[v].add(u)

    def DFSUtil(self, v, visited):
        visited[v] += 1
        # print(v)
        for i in self.graph[v]:
            if visited.get(i, 0) == 0:
                visited[i] = 0
                self.DFSUtil(i, visited)
            else:
                visited[i] += 1

    def DFS(self):
        visited = dict()
        visited2 = []
        for i in self.graph:
            if visited.get(i, 0) == 0:
                visited[i] = 0
                visited2.append(i)
                self.DFSUtil(i, visited)

        for j in visited2:
            visited[j] -= 1
        return visited

    def makeComunity(self):
        self.communityUtil()
        self.communityUtil2()

    def getCommunities(self, u):
        return self.communities[u]

    def communityUtil(self):
        for vertex1 in self.graph:
            vertex1_cits = self.graph[vertex1]
            for vertex2 in self.graph[vertex1]:
                vertex2_cits = self.graph[vertex2]
                intersection = vertex1_cits & vertex2_cits
                if len(intersection) >= 0.2 * len(vertex1_cits) or len(intersection) >= 0.2 * len(vertex2_cits):
                    self.communities[vertex1].add(vertex2)
                for vertex3 in self.graphIn[vertex2]:
                    vertex3_cits = self.graph[vertex3]
                    intersection = vertex1_cits & vertex3_cits
                    if len(intersection) >= 0.2 * len(vertex1_cits) or len(intersection) >= 0.2 * len(vertex2_cits):
                        self.communities[vertex1].add(vertex3)

        for vertex1 in self.graph:
            vertex1_cits = self.graph[vertex1]
            for vertex2 in self.graphIn[vertex1]:
                vertex2_cits = self.graph[vertex2]
                intersection = vertex1_cits & vertex2_cits
                if len(intersection) >= 0.2 * len(vertex1_cits) or len(intersection) >= 0.2 * len(vertex2_cits):
                    self.communities[vertex1].add(vertex2)


    def communityUtil2(self):
        for vertex1 in self.graph:
            vertex1_comm = self.communities[vertex1]
            for vertex2 in self.graph[vertex1]:
                vertex2_cits = self.graph[vertex2]
                intersection = vertex1_comm & vertex2_cits
                if len(intersection) >= 0.2 * len(vertex1_comm) or len(intersection) >= 0.2 * len(vertex2_cits):
                    self.communities[vertex1].add(vertex2)
                for vertex3 in self.graphIn[vertex2]:
                    vertex3_cits = self.graph[vertex3]
                    intersection = vertex1_comm & vertex3_cits
                    if len(intersection) >= 0.2 * len(vertex1_comm) or len(intersection) >= 0.2 * len(vertex2_cits):
                        self.communities[vertex1].add(vertex3)

        for vertex1 in self.graph:
            vertex1_comm = self.communities[vertex1]
            for vertex2 in self.graphIn[vertex1]:
                vertex2_cits = self.graph[vertex2]
                intersection = vertex1_comm & vertex2_cits
                if len(intersection) >= 0.2 * len(vertex1_comm) or len(intersection) >= 0.2 * len(vertex2_cits):
                    self.communities[vertex1].add(vertex2)

