import csv
from Graph_recursive_Class import Graph
g1 = Graph()
nodes = dict()
edges_file = open('edges.csv')
nodes_file = open('nodes.csv')
freq = dict()
edges_csv_reader = csv.reader(edges_file, delimiter=',')
nodes_csv_reader = csv.reader(nodes_file, delimiter=',')
flag = True
for edge in edges_csv_reader:
    if flag:
        flag = False
        continue
    g1.graph[int(edge[0])]
    g1.graph[int(edge[1])]
    g1.addEdge(int(edge[0]), int(edge[1]))
    freq[edge[1]] = freq.get(edge[1], 0) + 1

Papers = freq.items()
maxPapers = sorted(Papers, key=lambda tup: tup[1])
maxPapers.reverse()
for i in range(1):
    print(maxPapers[i])


