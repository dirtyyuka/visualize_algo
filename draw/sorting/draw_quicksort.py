import pygame

from .config import BG_COLOR, BAR_WIDTH, BAR_GAP, WIDTH, HEIGHT, COLORS, graph_setup

def draw_quick(screen, data, font, info):
    screen.fill(BG_COLOR)
    title = "draw_quicksort".replace("draw_", "")
    graph_setup(screen, font, title)

    for i, val in enumerate(data):
        x = i * (BAR_WIDTH + BAR_GAP)
        y = HEIGHT - val
        color = COLORS["default"]

        # ------ ACTIONS ------
        if info["action"] == "compare" and (i == info["i"] or i == info["j"]):
            color = COLORS["compare"]

        if info["k"] == i:
            color = COLORS["swap"]

        if i in info["placed"]:
            color = COLORS["sorted"]

        pygame.draw.rect(screen, color, (x, y, BAR_WIDTH, val))
    pygame.draw.line(screen, COLORS["x-line"], (0, HEIGHT - 1), (WIDTH, HEIGHT - 1), 5)
    pygame.display.flip()