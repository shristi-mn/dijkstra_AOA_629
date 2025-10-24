
# Adjacency list with node and it's neighbours marked along with the weights.
cstat_map = {
    1: [(2, 1), (11,1)],
    2: [(1,1), (3, 1),(21,1)],
    3: [(2,1), (4, 1), (8,2)],
    4: [(3,1), (5, 1)],
    5: [(22,1),(4,1),(7,1), (6, 2)],
    6: [(5,2), (7, 2)],
    7: [(5,1), (6, 2), (8, 1)],
    8: [(7,1), (9, 1), (3, 2)],
    9: [(8, 1), (19, 2),(10, 1)],
    10: [(11, 1), (9, 1), (18, 2)],
    11: [(1, 1), (10, 1), (12, 2), (17, 1)],
    12: [(11, 2), (13, 2)],
    13: [(12, 2), (14, 2), (21, 1)],
    14: [(13, 2), (15, 1),(16, 1),(20, 1)],
    15: [(14, 1)],
    16: [(14, 1), (17, 2)],
    17: [(16, 2), (11, 1), (18, 1)],
    18: [(17, 1), (19, 2), (10, 2)],
    19: [(18, 2), (9, 2)],
    20: [(14, 1), (21, 1), (22, 2)],
    21: [(2, 1), (13, 1), (20, 2), (22, 2)],
    22: [(5, 1), (20, 1), (21, 2)]
}

import heapq

def dijkstra(graph, source):
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    
    pq = [(0, source)]
    
    while pq:
        current_dist, u = heapq.heappop(pq)
        
        if current_dist > dist[u]:
            continue
        
        for v, weight in graph[u]:
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                heapq.heappush(pq, (dist[v], v))
    
    return dist

source = 1
targets = [6, 8, 9, 15, 16, 22]

distances = dijkstra(cstat_map, source)

print("Shortest distances from node", source)
for t in targets:
    if t in distances:
        print(f"To node {t}: {distances[t]}")
    else:
        print(f"To node {t}: No path found")
