import pygame
import sys
import os

from algorithms import *
from draw import *

from draw.graphs.config import data, WIDTH, HEIGHT

ALGORITHMS = {
    "bubble": bubble_sort,
    "merge": merge_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "quicksort": quick_sort,
    "bfs": bfs,
}

CURRENT_ALG = "bfs"

DRAW_MAP = {
    "bubble": draw_bubble,
    "merge": draw_merge,
    "selection": draw_selection,
    "insertion": draw_insertion,
    "quicksort": draw_quick,
    "bfs": draw_bfs,
}

def main():
    pygame.init()
    font = pygame.font.Font("fonts/JetBrainsMono-Medium.ttf", 48)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Algorithm Visualizer")

    clock = pygame.time.Clock()
    sorting = ALGORITHMS[CURRENT_ALG](data.copy(), 0)

    running = True
    sorting_done = False
    info = {}

    while running:
        clock.tick(2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not sorting_done:
            try:
                arr, info = next(sorting)
            except StopIteration:
                sorting_done = True
                info = {"i": None, "j": None, "action": "done", "sorted": len(data)}
                arr = data  # add here so arr is always defined
        else:
            arr = data

        DRAW_MAP[CURRENT_ALG](screen, arr, font, info)

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
