def dfs(graph):
    visited = {}
    discovery = {}
    finish = {}
    time = [0]
    parent = {}
    topo = []

    for node in graph:
        visited[node] = False
        parent[node] = None

    def dfs_visit(u):
        time[0] += 1
        discovery[u] = time[0]
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                dfs_visit(v)
        time[0] += 1
        finish[u] = time[0]
        topo.insert(0, u)

    for u in graph:
        if not visited[u]:
            dfs_visit(u)

    print("\nDFS Discovery/Finish Times:")
    for u in graph:
        print(f"{u}: d={discovery[u]}, f={finish[u]}")

    return topo  


def topological_sort(graph):
    return dfs(graph)


def kruskal_mst(edges, vertices):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    edges.sort()
    mst = []

    for w, u, v in edges:
        if find(u) != find(v):
            mst.append((u, v, w))
            ru, rv = find(u), find(v)
            if ru != rv:
                if rank[ru] < rank[rv]:
                    parent[ru] = rv
                elif rank[ru] > rank[rv]:
                    parent[rv] = ru
                else:
                    parent[rv] = ru
                    rank[ru] += 1
    return mst


graph = {
    'u': ['v', 'x'],
    'v': ['y'],
    'x': ['v'],
    'y': ['x'],
    'w': ['y', 'z'],
    'z': ['z']
}

topo = topological_sort(graph)
print("\nTopological Sort:", topo)
print()
edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]
vertices = {0, 1, 2, 3}
mst = kruskal_mst(edges, vertices)
print("Kruskal MST:", mst)
print()
