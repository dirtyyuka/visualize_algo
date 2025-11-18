def bfs(graph, start):
    from collections import deque

    visited = set()
    queue = deque([start])

    # first frame
    yield graph, {"action": "start", "node": start, "queue": [start], "visited": []}

    while queue:
        node = queue.popleft()

        yield graph, {"action": "visit", "node": node, "queue": list(queue), "visited": list(visited)}

        for neighbor in graph[node]:
            yield graph, {"action": "explore", "node": node, "neighbor": neighbor,
                          "queue": list(queue), "visited": list(visited)}

            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

                yield graph, {"action": "enqueue", "node": node, "neighbor": neighbor,
                    "queue": list(queue), "visited": list(visited)}

    yield graph, {"action": "done", "visited": list(visited)}