import pygame

from .config import BG_COLOR, UI_HEIGHT, WIDTH, HEIGHT, COLORS, center_positions, title

def draw_bfs(screen, graph, font_m, font_s, info):
    node_pos = center_positions()
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    title(screen, font_m, font_s, ["visited", "in_queue", "default", "current"], "BFS")

    for a in graph:
        for b in graph[a]:
            pygame.draw.line(screen, (200, 200, 200), node_pos[a], node_pos[b], 2)

    for node, pos in node_pos.items():
        color = COLORS["default"]

        if node in info.get("visited", []):
            color = COLORS["visited"]

        if node in info.get("queue", []):
            color = COLORS["in_queue"]

        if node == info.get("node"):
            color = COLORS["current"]

        pygame.draw.circle(screen, color, pos, 35)

        #render node number
        text_surf = font_m.render(str(node), True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=pos)

        screen.blit(text_surf, text_rect)

    pygame.display.flip()