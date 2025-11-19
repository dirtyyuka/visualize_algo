import pygame

from .config import COLORS, title, center_positions

def draw_bfs(screen, graph, font_m, font_s, info):
    node_pos = center_positions()
    screen.fill((30, 30, 30))
    text = "draw_bfs".replace("draw_", "")
    title(screen, font_m, font_s, text)

    for a in graph:
        for b in graph[a]:
            pygame.draw.line(screen, (200, 200, 200), node_pos[a], node_pos[b], 2)

    for node, pos in node_pos.items():
        color = COLORS["node"]

        if node in info.get("visited", []):
            color = COLORS["visited"]

        if node in info.get("queue", []):
            color = COLORS["frontier"]

        if node == info.get("node"):
            color = COLORS["current"]

        pygame.draw.circle(screen, color, pos, 40)

        #render node number
        text_surf = font_m.render(str(node), True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=pos)

        screen.blit(text_surf, text_rect)

    pygame.display.flip()