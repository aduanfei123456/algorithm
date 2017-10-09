"""
Given a directed graph, check whether it contains a cycle.
Real-life scenario: deadlock detection in a system. Processes may be
represented by vertices, then and an edge A -> B could mean that process A is
waiting for B to release its lock on a resource.
"""
from enum import Enum


class TraversalState(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


example_graph_with_cycle = {'A': ['B', 'C'],
                            'B': ['D'],
                            'C': ['F'],
                            'D': ['E', 'F'],
                            'E': ['B'],
                            'F': []}

example_graph_without_cycle = {'A': ['B', 'C'],
                               'B': ['D', 'E'],
                               'C': ['F'],
                               'D': ['E'],
                               'E': [],
                               'F': []}

def cycle_detection(graphs):
    detected=[]
    detecting=[]
    incircle=isin_circle(graphs,'A',detected,detecting)
    return incircle
def isin_circle(graphs,key,detected,detecting):
    incircle=False
    for neighbor in graphs[key]:
        if neighbor not in detected:
            if neighbor in detecting:
                return True
            else:
                detecting.append(neighbor)
                incircle=incircle or isin_circle(graphs,neighbor,detected,detecting)
                detecting.pop()
                detected.append(neighbor)
    return incircle           
print(cycle_detection(example_graph_without_cycle))



