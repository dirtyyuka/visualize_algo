import pygame

WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 40
BAR_GAP = 5
BG_COLOR = (30, 30, 30)

data = [50, 100, 200, 150, 300, 250, 400, 350, 29, 51, 91, 35, 20, 291, 348, 158, 477]

COLORS = {
    "default": (100, 200, 255),
    "compare": (255, 100, 100),
    "swap": (255, 180, 80),
    "sorted": (100, 255, 100),
    "pivot": (255, 255, 120),
    "merge": (180, 120, 255),
    "x-line": (200, 200, 200),
}

def graph_setup(screen, font, alg):
    # ------ DRAW VERTICAL LINES ------
    for i in range(len(data) + 1):
        x = i * (BAR_WIDTH + BAR_GAP) + 25
        pygame.draw.line(screen, (50, 50, 50), (x, 25), (x, HEIGHT))

    # ------ Algorithm Title ------
    surf = font.render(alg.capitalize() + "SORT", True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH // 2, 40))
    screen.blit(surf, rect)