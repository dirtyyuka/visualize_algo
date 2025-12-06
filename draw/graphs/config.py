import pygame

data = [{0: [(1, 4)], 1:[(2, 5)], 2: [(3, 8)],
            3: [(4, 5)], 4: [(5, 8)],5: []},
            {0: [1, 2],1: [3, 4],2: [5],3: [], 4: [5],5: []}]

WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 40
BAR_GAP = 5
UI_HEIGHT = 80 + 1
BG_COLOR = (30, 30, 30)

COLORS = {
    "default": (170, 200, 255),   # light blue
    "visited": (80, 120, 255),    # blue
    "in_queue": (255, 200, 80),   # orange
    "checking": (255, 120, 120),  # red
    "path": (120, 255, 120),      # bright green
    "start": (100, 255, 100),
    "end": (255, 100, 255),
    "current": (80, 255, 255),
    "color1": (230, 50, 50),
    "color2": (50, 180, 230),
    "color3": (80, 200, 120),
    "color4": (240, 200, 40),
    "color5": (160, 80, 220)
}

NODE_POS = {
    0: (100, 100),
    1: (300, 100),
    2: (500, 100),
    3: (100, 300),
    4: (300, 300),
    5: (500, 300),
}

def center_positions():
    xs = [p[0] for p in NODE_POS.values()]
    ys = [p[1] for p in NODE_POS.values()]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    layout_width = max_x - min_x
    layout_height = max_y - min_y

    #offset needed
    offset_x = WIDTH // 2 - (min_x + layout_width // 2)

    graph_center_y = UI_HEIGHT + (HEIGHT - UI_HEIGHT) // 2
    offset_y = graph_center_y - (min_y + layout_height // 2)

    #apply offset
    return {n: (x + offset_x, y+offset_y) for n, (x, y) in NODE_POS.items()}

def title(screen, font_m, font_s, stats, alg):
    # ------ Algorithm Title ------
    surf = font_m.render(alg.upper(), True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH // 2, 120))

    # ------ render node states ------
    stats_surf = [font_s.render(s, True, (255, 255, 255)) for s in stats]

    max_width = max(s.get_width() for s in stats_surf)

    # left edge for alignment
    left_edge = 45
    top_edge = 100

    # create rects
    stats_rects = []
    for s in stats_surf:
        stats_rects.append(s.get_rect(left=left_edge, top=top_edge))
        top_edge += 30

    # title
    screen.blit(surf, rect)

    # ------ STATS RECTS ------
    for s, r in zip(stats_surf, stats_rects):
        screen.blit(s, r)

    circle_x = 25
    radius = 5

    for i, s in enumerate(stats_rects):
        pygame.draw.circle(screen, COLORS[f"{stats[i]}"], (circle_x, s.centery), radius)
