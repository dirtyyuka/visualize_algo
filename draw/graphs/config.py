import pygame

data = {0: [1, 2], 1: [3, 4], 2: [5], 3: [], 4: [], 5: []}

WIDTH, HEIGHT = 800, 600

COLORS = {
    "node": (120, 180, 255),
    "visited": (100, 255, 100),
    "frontier": (255, 170, 80),
    "current": (255, 100, 100)
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
    offset_y = HEIGHT // 2 - (min_y + layout_height // 2)

    #apply offset
    return {n: (x + offset_x, y+offset_y) for n, (x, y) in NODE_POS.items()}

def title(screen, font_m, font_s, alg):
    # ------ Algorithm Title ------
    surf = font_m.render(alg.upper(), True, (255, 255, 255))
    rect = surf.get_rect(center=(WIDTH // 2, 40))

    # ------ render node states ------
    in_queue = font_s.render("in queue", True, (255, 255, 255))
    visited = font_s.render("visited", True, (255, 255, 255))
    default = font_s.render("default", True, (255, 255, 255))

    queue_rect = in_queue.get_rect(topright=(WIDTH - 25, 20))
    visited_rect = visited.get_rect(topright=(WIDTH - 25, 50))
    default_rect = default.get_rect(topright=(WIDTH - 25, 80))

    # ------ draw text ------
    screen.blit(surf, rect)
    screen.blit(in_queue, queue_rect)
    screen.blit(visited, visited_rect)
    screen.blit(default, default_rect)

    # ------ stats circle ------
    left_x = min(queue_rect.left, visited_rect.left, default_rect.left)
    circle_x = left_x - 20
    radius = 5

    pygame.draw.circle(screen, COLORS["frontier"], (circle_x, queue_rect.centery), radius)
    pygame.draw.circle(screen, COLORS["visited"], (circle_x, visited_rect.centery), radius)
    pygame.draw.circle(screen, COLORS["node"], (circle_x, default_rect.centery), radius)