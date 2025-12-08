import pygame
from .config import SQUARE, BG_COLOR, UI_HEIGHT, WIDTH, HEIGHT, COLORS, graph_setup

def draw_sw(screen, data, font_m, font_s, info):
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT))
    graph_setup(screen, font_m, font_s, "Sliding Window")

    detail1 = font_s.render("Subarray count:", True, (255, 255, 255))
    detail1_rect = detail1.get_rect(center=(WIDTH//2 - 100, HEIGHT//2 - 60))

    detail2 = font_s.render(f"Target: {info.get("target")}", True, (255, 255, 255))
    detail2_rect = detail2.get_rect(center=(WIDTH//2 + 100, HEIGHT//2 - 60))

    screen.blit(detail1, detail1_rect)
    screen.blit(detail2, detail2_rect)
    n = len(data)
    arr_size = SQUARE * n
    for i in range(n):
        color = COLORS["default"]
        if info.get("i") < i <= info.get("j"):
            color = COLORS["in_window"]

        clear_rect = pygame.Rect(detail1_rect.right + 5, detail1_rect.top, 30, detail1_rect.height)
        pygame.draw.rect(screen, BG_COLOR, clear_rect)

        count = font_s.render(str(info.get("count")), True, (255, 255, 255))
        count_rect = count.get_rect(midleft=(detail1_rect.right + 5, detail1_rect.centery))
        screen.blit(count, count_rect)
        
        x = (WIDTH // 2) - (arr_size // 2) + i * SQUARE
        y = (HEIGHT // 2)
        pygame.draw.rect(screen, color, (x, y, SQUARE, SQUARE))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, SQUARE, SQUARE), width=1)
        text = font_m.render(str(data[i]), True, (0, 0, 0))
        screen.blit(text, text.get_rect(center=(x + SQUARE//2, y + SQUARE//2)))
        
    