import pygame

from .config import BG_COLOR, UI_HEIGHT, WIDTH, HEIGHT, COLORS, center_positions, title

def group_colors(parent):
    roots = {}
    colors = {}

    next_color = 0
    palette = [
        (230, 50, 50),
        (50, 180, 230),
        (80, 200, 120),
        (240, 200, 40),
        (160, 80, 220)
    ]

    for node in range(len(parent)):
        root = parent[node]
        if root not in roots:
            roots[root] = palette[next_color % len(palette)]
            next_color += 1
        colors[node] = roots[root]

    return colors

def draw_unionfind(screen, graph, font_m, font_s, info):
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    title(screen, font_m, font_s, ["color1", "color2", "color3", "color4", "color5"], "Union Find")

    node_pos = center_positions()
    parent = info.get("parent")
    pair = info.get("pair")

    # ------ SET COLORS ------
    colors = group_colors(parent)

    for a in graph:
        for b, _ in graph[a]:
            color = (200, 200, 200)

            if pair == (a, b):
                color = (255, 100, 100)

            pygame.draw.line(screen, color, node_pos[a], node_pos[b], 3)

    for node in node_pos:
        pygame.draw.circle(screen, colors[node], node_pos[node], 35)
        label = font_m.render(str(node), True, (0, 0, 0))
        screen.blit(label, label.get_rect(center=node_pos[node]))

    pygame.display.flip()