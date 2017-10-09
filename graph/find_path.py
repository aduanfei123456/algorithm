myGraph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

# find path from start to end using recursion with backtracking
import copy
def find_path(graph,begin,end,path=[],paths=[]):
    path.append(begin)
    if begin==end:
        return True
    findStatus=False
    for neighbor in graph[begin]:
        if neighbor not in path:
            findStatus=find_path(graph,neighbor,end,path,paths,)
        if findStatus:
            paths.append(copy.deepcopy(path))

    path.pop()
    return False
def find_all_path(graph,start,end,passed=[],path=[],paths=[]):
    path.append(start)
    print(start,path)
    passed.append(start)
    if start==end:
        paths.append(copy.deepcopy(path))

    else:
        for neighbor in graph[start]:
            if neighbor not in path:
                find_all_path(graph,neighbor,end,passed,path,paths)
    path.pop()
    return paths

'''def find_all_path(graph, start, end, path=[]):
    path = path + [start]
    print(path)
    if (start == end):
        return [path]
    if not start in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
'''
myGraph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D', 'F'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
print(find_all_path(myGraph,'A','F'))

