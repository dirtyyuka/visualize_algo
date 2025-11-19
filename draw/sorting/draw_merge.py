import pygame

from .config import BAR_WIDTH, BG_COLOR, UI_HEIGHT, BAR_GAP, WIDTH, HEIGHT, COLORS, graph_setup

def draw_merge(screen, data, font_m, font_s, info):
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT - UI_HEIGHT))
    title = "draw_merge".replace("draw_", "")
    graph_setup(screen, font_m, font_s, title)

    for i, val in enumerate(data):
        x = i * (BAR_WIDTH + BAR_GAP) + 25
        y = HEIGHT - val
        color = COLORS["default"]

        if info["action"] == "compare":
            if i == info["a"] or i == info["b"]:
                color = COLORS["compare"]

        if info.get("i") is not None and info.get("k") is not None:
            if info["i"] <= i < info["k"]:
                color = COLORS["sorted"]

        pygame.draw.rect(screen, color, (x, y, BAR_WIDTH, val))
    pygame.draw.line(screen, COLORS["x-line"], (0, HEIGHT - 1), (WIDTH, HEIGHT - 1), 5)
    pygame.display.flip()