def dijkstra(graph, start, end):
    import heapq

    # ------ STATE ARRAYS ------
    dist = [float('inf')] * len(graph)
    prev = [None] * len(graph)
    visited = set()

    dist[start] = 0
    pq = [(0, start)]

    # first frame
    yield graph, {
        "action": "start", "node": start, "end": end, "visited": [],
        "dist": dist.copy(), "queue": sorted(pq), "path": []
    }

    while pq:
        current_dist, node = heapq.heappop(pq)

        # outdated entries
        if dist[node] < current_dist:
            continue

        visited.add(node)

        # current state
        yield graph, {
            "action": "check", "node": node, "end": end, "visited": list(visited),
            "dist": dist.copy(), "queue": sorted(pq), "path": []
        }

        if node == end:
            break

        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight

            # explore neighbor
            yield graph, {
                "action": "explore", "node": node, "end": end, "visited": list(visited),
                "dist": dist.copy(), "queue": sorted(pq), "path": [], "neighbor": neighbor,
            }

            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                prev[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

                # yield state
                yield graph, {
                    "action": "relax", "node": node, "neighbor": neighbor,
                    "end": end, "visited": list(visited), "dist": dist.copy(), "queue": sorted(pq), "path": []
                }

    # ------ RECONSTRUCT PATH ------
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    # final frame
    yield graph, {
        "action": "done", "node": end, "end": end, "dist": dist.copy(),
        "visited": list(visited), "queue": sorted(pq), "path": path
    }