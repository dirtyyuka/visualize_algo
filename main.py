import pygame
import sys

from algorithms import *
from draw import *

from draw.basic.config import data, WIDTH, HEIGHT

ALGORITHMS = {
    "bubble": bubble_sort,
    "merge": merge_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "quicksort": quick_sort,
    "bfs": bfs,
    "dfs": dfs,
    "dijkstra": dijkstra,
    "unionfind": unionfind,
    "avl": avl_generator,
    "sw": slidingwindow,
}

DRAW_MAP = {
    "bubble": draw_bubble,
    "merge": draw_merge,
    "selection": draw_selection,
    "insertion": draw_insertion,
    "quicksort": draw_quick,
    "bfs": draw_bfs,
    "dfs": draw_dfs,
    "dijkstra": draw_dijkstra,
    "unionfind": draw_unionfind,
    "avl": draw_avl,
    "sw": draw_sw,
}

CURRENT_ALG = "sw"
UI_HEIGHT = 80
BG_COLOR = (30, 30, 30)

class UIButton:
    def __init__(self, text, x, y, font, padding=10):
        self.text = text
        self.font = font
        self.color = (70, 70, 70)
        self.hover_color = (120, 120, 120)

        self.surface = font.render(text, True, (255, 255, 255))
        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
        self.rect.inflate_ip(padding * 2, padding * 2)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse_pos)

        pygame.draw.rect(screen,
            self.hover_color if is_hover else self.color,
            self.rect,
            border_radius=10
        )

        screen.blit(self.surface, self.surface.get_rect(center=self.rect.center))

    def clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

def main():
    pygame.init()
    font_m = pygame.font.Font("fonts/JetBrainsMono-Medium.ttf", 32)
    font_s = pygame.font.Font("fonts/JetBrainsMono-Light.ttf", 16)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer")

    screen.fill(BG_COLOR)

    # ------ UI ------
    btn_play = UIButton("▶ Play", 60, 25, font_s)
    btn_pause = UIButton("⏸ Pause", 60, 25, font_s)
    btn_step = UIButton("Step →", 190, 25, font_s)
    btn_restart = UIButton("⟳ Restart", 340, 25, font_s)

    btn_speed1 = UIButton("1x", 540, 25, font_s)
    btn_speed2 = UIButton("2x", 600, 25, font_s)
    btn_speed4 = UIButton("4x", 660, 25, font_s)
    btn_speed8 = UIButton("8x", 720, 25, font_s)

    clock = pygame.time.Clock()
    sorting = ALGORITHMS[CURRENT_ALG](data, 10)
    current_arr, info = next(sorting)

    running = True

    paused= False
    step_once = False
    speed = 1
    frame_counter = 0

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # ------ UI handlers ------
            if event.type == pygame.MOUSEBUTTONDOWN:
                if paused:
                    if btn_play.rect.collidepoint(event.pos):
                        paused = False
                else:
                    if btn_pause.rect.collidepoint(event.pos):
                        paused = True

                if btn_step.clicked(event):
                    paused = True
                    step_once = True

                if btn_restart.clicked(event):
                    info = {}
                    paused = False
                    step_once = False
                    sorting = ALGORITHMS[CURRENT_ALG](data, 10)
                    current_arr, info = next(sorting)

            if btn_speed1.clicked(event): speed = 1
            if btn_speed2.clicked(event): speed = 2
            if btn_speed4.clicked(event): speed = 4
            if btn_speed8.clicked(event): speed = 8

        # ------ CONTINUE GENERATOR -------
        if not paused:
            frame_counter += 1
            if frame_counter >= (10 // speed):
                try:
                    current_arr, info = next(sorting)
                except StopIteration:
                    paused = True
                frame_counter = 0

        elif step_once:
            try:
                current_arr, info = next(sorting)
            except StopIteration:
                paused = True
            step_once = False

        DRAW_MAP[CURRENT_ALG](screen, current_arr, font_m, font_s, info)

        # ------ UI ------
        pygame.draw.rect(screen, (40, 40, 40), (0, 0, WIDTH, UI_HEIGHT))
        pygame.draw.line(screen, (80, 80, 80), (0, UI_HEIGHT), (WIDTH, UI_HEIGHT))

        # ------ DRAW BUTTONS ------
        if paused:
            btn_play.draw(screen)
        else:
            btn_pause.draw(screen)

        btn_restart.draw(screen)
        btn_step.draw(screen)

        btn_speed1.draw(screen)
        btn_speed2.draw(screen)
        btn_speed4.draw(screen)
        btn_speed8.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
