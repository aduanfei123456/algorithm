# Minimum spanning tree (MST) is going to use an undirected graph
#
# The disjoint set is represented with an list <n> of integers where
# <n[i]> is the parent of the node at position <i>.
# If <n[i]> = <i>, <i> it's a root, or a head, of a set
class Edge:
    def __init__(self,u,v,weight):
        self.u=u
        self.v=v
        self.weight=weight
class DisjointSet:
    def __init__(self,n):
        self.parent=[0]*n

        for i in range(n):
            self.parent[i]=i

    def mergeSet(self,a,b):
        self.parent[a]=b
    def findSet(self,a):
        #find the edge node
        if not self.parent[a]==a:
            self.parent[a]==self.findSet(self.parent[a])
        return self.parent[a]

def kruskal(n,edges,ds):
    edges.sort(key=lambda edge:edge.weight)
    re_edges=[]
    for edge in edges:
        edge_u=ds.findSet(edge.u)
        edge_v=ds.findSet(edge.v)
        if not edge_u==edge_v:
            re_edges.append(edge)
            ds.mergeSet(edge_u,edge_v)
            if len(re_edges)==n-1:
                break

    return sum([edge.weight for edge in re_edges])

























