import pygame

from .config import BAR_WIDTH, BG_COLOR, UI_HEIGHT, BAR_GAP, WIDTH, HEIGHT, COLORS, graph_setup

def draw_bubble(screen, data, font_m, font_s, info):
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    title = "draw_bubble".replace("draw_", "")
    graph_setup(screen, font_m, font_s, title)

    for i, val in enumerate(data):
        x = i * (BAR_WIDTH + BAR_GAP)
        y = HEIGHT - val
        color = COLORS["default"]
        if info.get("i") == i or info.get("j") == i:
            color = COLORS[info["action"]]
        elif info.get("sorted") is not None and i >= len(data) - info.get("sorted"):
            color = COLORS["sorted"]
        pygame.draw.rect(screen, color, (x, y, BAR_WIDTH, val))
    pygame.draw.line(screen, COLORS["x-line"], (0, HEIGHT - 1), (WIDTH, HEIGHT - 1), 5)
    pygame.display.flip()