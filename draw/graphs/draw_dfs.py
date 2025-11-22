import pygame

from .config import BG_COLOR, UI_HEIGHT, WIDTH, HEIGHT, COLORS, center_positions, title

def draw_dfs(screen, graph, font_m, font_s, info):
    node_pos = center_positions()
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    title(screen, font_m, font_s, ["checking", "visited", "default", "current"], "DFS")

    for a in graph:
        for b in graph[a]:
            pygame.draw.line(screen, (200, 200, 200), node_pos[a], node_pos[b], 2)

    for node, pos in node_pos.items():
        color = COLORS["default"]

        if node in info.get("visited", []):
            color = COLORS["visited"]

        if node == info.get("node"):
            color = COLORS["current"]

        if node == info.get("neighbor"):
            color = COLORS["in_queue"]

        pygame.draw.circle(screen, color, pos, 35)

        #render node number
        text_surf = font_m.render(str(node), True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=pos)

        screen.blit(text_surf, text_rect)

    pygame.display.flip()