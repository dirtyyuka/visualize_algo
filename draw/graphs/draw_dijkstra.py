import pygame

from .config import BG_COLOR, UI_HEIGHT, WIDTH, HEIGHT, COLORS, center_positions, title

def draw_dijkstra(screen, graph, font_m, font_s, info):
    node_pos = center_positions()
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    title(screen, font_m, font_s, ["start", "current", "visited", "in_queue", "end", "default"], "dijkstra")

    for a in graph:
        for b, w in graph[a]:
            ax, ay = node_pos[a]
            bx, by = node_pos[b]

            pygame.draw.line(screen, (200, 200, 200), node_pos[a], node_pos[b], 2)

            # ------ WEIGHT TAG ------
            mid_x = (ax + bx) // 2
            mid_y = (ay + by) // 2

            weight_surf = font_s.render(str(w), True, (255, 255, 255))
            weight_rect = weight_surf.get_rect(center=(mid_x + 12, mid_y - 12))

            screen.blit(weight_surf, weight_rect)

    for node, pos in node_pos.items():
        color = COLORS["default"]

        if info.get("end") == node:
            color = COLORS["end"]

        if info.get("start") == node:
            color = COLORS["start"]

        if info.get("queue") is not None:
            for _, n in info.get("queue"):
                if n == node:
                    color = COLORS["in_queue"]

        if info.get("node") == node:
            color = COLORS["current"]

        if node in info.get("visited", []):
            color = COLORS["visited"]

        if node in info.get("path", []):
            color = COLORS["path"]

        pygame.draw.circle(screen, color, pos, 35)

        # render node number
        text_surf = font_m.render(str(node), True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=pos)

        screen.blit(text_surf, text_rect)

    pygame.display.flip()

