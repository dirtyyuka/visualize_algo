WIDTH, HEIGHT = 800, 600
SQUARE = 60
UI_HEIGHT = 80 + 1
BG_COLOR = (30, 30, 30)

COLORS = {
    "default": (100, 200, 255),
    "in_window": (100, 255, 100)
}

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def graph_setup(screen, font_m, font_s, alg):
    # ------ Algorithm Title ------
    surf = font_m.render(alg.capitalize(), True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH // 2, 180))
    
    screen.blit(surf, rect)