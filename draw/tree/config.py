WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 40
BAR_GAP = 5
UI_HEIGHT = 80 + 1
BG_COLOR = (30, 30, 30)

data = [1, 2, 3, 4, 5, 6, 7]

COLORS = {
    "default": (100, 200, 255),
    "insert": (255, 200, 0),
    "rotate": (255, 120, 120)
}

def graph_setup(screen, font_m, font_s, alg):
    # ------ Algorithm Title ------
    surf = font_m.render(alg.capitalize() + "Tree", True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH // 2, 120 ))
    screen.blit(surf, rect)