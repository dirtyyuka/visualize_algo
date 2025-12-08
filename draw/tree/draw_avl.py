import pygame
from typing import Optional

from .config import (
    BAR_WIDTH,
    BG_COLOR,
    UI_HEIGHT,
    BAR_GAP,
    WIDTH,
    HEIGHT,
    COLORS,
    graph_setup,
)


class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    height: int = 1


def draw_avl(screen, tree, font_m, font_s, info):
    pygame.draw.rect(screen, BG_COLOR, (0, UI_HEIGHT, WIDTH, HEIGHT - UI_HEIGHT))
    graph_setup(screen, font_m, font_s, "AVL")

    if not tree:
        pygame.display.flip()
        return

    # ------ find the root ------
    def find_root(tree_dict: dict):
        all_nodes = set(tree_dict.keys())
        children = set()
        for k, v in tree_dict.items():
            if v["left"]:
                children.add(v["left"])
            if v["right"]:
                children.add(v["right"])
        return list(all_nodes - children)[0]

    root = find_root(tree)

    # ------ layout position ------
    def layout_tree(
        tree_dict: dict, root_key: Node, screen_width, top_y=200, level_gap=120
    ):
        pos = {}

        def assign_pos(node, depth, x_min, x_max):
            if node is None:
                return
            x = (x_min + x_max) // 2
            y = top_y + depth * level_gap
            pos[node] = (x, y)
            left = tree_dict[node]["left"]
            right = tree_dict[node]["right"]
            assign_pos(left, depth + 1, x_min, x + 40)
            assign_pos(right, depth + 1, x - 40, x_max)

        assign_pos(root, 0, 60, screen_width - 60)
        return pos

    positions = layout_tree(tree, root, WIDTH)

    edge_color = (200, 200, 200)

    text = font_s.render("Inserting:", True, (255, 255, 255))
    rect = text.get_rect(topleft=(30, UI_HEIGHT + 30))
    screen.blit(text, rect)
    if info.get("action") == "inserted":
        key = info["key"]
        node = font_s.render(str(key), True, (255, 255, 255))
        screen.blit(
            node, node.get_rect(topleft=(rect.width + 30 + 10, UI_HEIGHT + 30))
        )  # the number being inserted
    else:
        none_text = font_s.render("None", True, (255, 255, 255))
        screen.blit(
            none_text,
            none_text.get_rect(topleft=(rect.width + 30 + 10, UI_HEIGHT + 30)),
        )
    
    text2 = font_s.render("Rotation:", True, (255, 255, 255))
    rect2 = text2.get_rect(topleft=(30, UI_HEIGHT + 60))
    screen.blit(text2, rect2)
    if info.get("action") == "rotate":
        type = info.get("rotation")
        node = font_s.render(type, True, (255, 255, 255))
        screen.blit(
            node, node.get_rect(topleft=(rect2.width + 30 + 20, UI_HEIGHT + 60))
        )  # the number being inserted
    else:
        none_text = font_s.render("None", True, (255, 255, 255))
        screen.blit(
            none_text,
            none_text.get_rect(topleft=(rect2.width + 30 + 20, UI_HEIGHT + 60)),
        )

    for parent, info_node in tree.items():
        px, py = positions[parent]

        left = info_node["left"]
        right = info_node["right"]

        if left is not None:
            lx, ly = positions[left]
            pygame.draw.line(screen, edge_color, (px, py), (lx, ly), 4)

        if right is not None:
            rx, ry = positions[right]
            pygame.draw.line(screen, edge_color, (px, py), (rx, ry), 4)

    # ------ draw edges ------
    for k, (x, y) in positions.items():
        # color based on event
        color = COLORS["default"]
        if info.get("action") == "inserted" and info["key"] == k:
            color = COLORS["insert"]
        if info.get("action") == "rotate" and k in info.get("affected", []):
            color = COLORS["rotate"]

        pygame.draw.circle(screen, color, (x, y), 35)

    text = font_m.render(str(k), True, (0, 0, 0))
    screen.blit(text, text.get_rect(center=(x, y)))
  
  pygame.display.flip()



        text = font_m.render(str(k), True, (0, 0, 0))
        screen.blit(text, text.get_rect(center=(x, y)))

    pygame.display.flip()
