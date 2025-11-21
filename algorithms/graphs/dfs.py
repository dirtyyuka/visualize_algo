def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # first frame
    yield graph, {"action": "visit", "node": start, "visited": list(visited)}

    visited.add(start)

    for neighbor in graph[start]:
        yield graph, {
            "action": "check",
            "node": start,
            "neighbor": neighbor,
            "visited": list(visited),
        }

        if neighbor not in visited:
            yield from dfs(graph, neighbor, visited)

    yield graph, {"action": "backtrack", "node": start, "visited": list(visited)}
