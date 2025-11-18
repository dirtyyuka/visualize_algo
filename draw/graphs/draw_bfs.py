import pygame

from .config import NODE_POS, COLORS

def draw_bfs(screen, graph, font, info):
    screen.fill((30, 30, 30))

    for a in graph:
        for b in graph[a]:
            pygame.draw.line(screen, (200, 200, 200), NODE_POS[a], NODE_POS[b], 2)

    for node, pos in NODE_POS.items():
        color = COLORS["node"]

        if node in info.get("visited", []):
            color = COLORS["visited"]

        if node in info.get("queue", []):
            color = COLORS["frontier"]

        if node == info.get("node"):
            color = COLORS["current"]

        pygame.draw.circle(screen, color, pos, 20)

    pygame.display.flip()