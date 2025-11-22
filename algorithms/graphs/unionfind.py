def unionfind(graph):
    parent = [i for i in range(len(graph))]
    rank = [0] * len(graph)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # initial frame
    yield graph, {"action": "start", "parent": parent.copy(), "pair": None}

    for a in graph:
        for b, _ in graph[a]:

            # consider edge
            yield graph, {"action": "check", "parent": parent.copy(), "pair": (a, b)}

            union(a, b)

            yield graph, {"action": "union", "parent": parent.copy(), "pair": (a, b)}

    yield graph, {"action": "done", "parent": parent.copy(), "pair": None}


