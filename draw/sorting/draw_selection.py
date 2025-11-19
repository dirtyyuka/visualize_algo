import pygame

from .config import BAR_WIDTH, BG_COLOR, UI_HEIGHT, BAR_GAP, WIDTH, HEIGHT, COLORS, graph_setup

def draw_selection(screen, data, font_m, font_s, info):
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    title = "draw_selection".replace("draw_", "")
    graph_setup(screen, font_m, font_s, title)

    for i, val in enumerate(data):
        x = i * (BAR_WIDTH + BAR_GAP)
        y = HEIGHT - val
        color = COLORS["default"]
        if info.get("action") == "compare" and (i == info.get("i") or i == info.get("j")):
            color = COLORS["compare"]

        if info.get("action") == "swap" and (i == info.get("i") or i == info.get("j")):
            color = COLORS["swap"]

        if info.get("sorted") is not None and i < info.get("sorted"):
            color = (100, 255, 100)

        pygame.draw.rect(screen, color, (x, y, BAR_WIDTH, val))
    pygame.draw.line(screen, COLORS["x-line"], (0, HEIGHT - 1), (WIDTH, HEIGHT - 1), 5)
    pygame.display.flip()