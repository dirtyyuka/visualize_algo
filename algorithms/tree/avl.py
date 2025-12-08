from typing import Optional, Dict, Any, List, Tuple 
class Node:
    def __init__(self, key: int):
      self.key: int = key
      self.left: Optional["Node"] = None
      self.right: Optional["Node"] = None
      self.height: int = 1

def height(n: Optional["Node"]) -> int:
    return 0 if n is None else n.height

def update_height(n: Node) -> None:
    n.height = 1 + max(height(n.left), height(n.right))

def balance_factor(n: Node) -> int:
    return height(n.left) - height(n.right)

def rotate_right(y: Node) -> Node:
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x: Node) -> Node:
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    update_height(x)
    update_height(y)
    return y

def node_to_dict(root: Optional[Node]) -> Dict[int, Dict[str, Any]]:
    # ------ CONVERT TREE TO DICT ------
    out = {}
    def walk(n):
        if not n:
            return
        out[n.key] = {
            "left": n.left.key if n.left else None,
            "right": n.right.key if n.right else None,
            "height": n.height
        }
        walk(n.left); walk(n.right)
    walk(root)
    return out

def avl_insert(root: Optional[Node], key: int) -> Tuple[Optional[Node], List[Dict]]:
    # ------ RECORD EVENTS ------
    events = []

    def _insert(node):
        if node is None:
            events.append({
                "type": "insert",
                "node_to_dict": None,
                "rotation": "None",
                "affected": [key]
            })
            return Node(key)
        if key < node.key:
            node.left = _insert(node.left)
        elif key > node.key:
            node.right = _insert(node.right)
        else:
            return node
        
        update_height(node)
        bf = balance_factor(node)
        if bf > 1 and key < node.left.key:
            events.append({"type": "rotate", "node_to_dict": node_to_dict(root), "rotation": "LL", "node": node.key, "affected": [node.key, node.left.key]})
            return rotate_right(node)
        if bf < -1 and key > node.right.key:
            events.append({"type": "rotate", "node_to_dict": node_to_dict(root), "rotation": "RR", "node": node.key, "affected": [node.key, node.right.key]})
            return rotate_left(node)
        if bf > 1 and key > node.left.key:
            events.append({"type": "rotate", "node_to_dict": node_to_dict(root), "rotation": "LR", "node": node.key, "affected": [node.key, node.left.key]})
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if bf < -1 and key < node.right.key:
            events.append({"type": "rotate", "node_to_dict": node_to_dict(root), "rotation": "RL", "node": node.key, "affected": [node.key, node.right.key]})
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node

    new_root = _insert(root)
    return new_root, events

def avl_generator(values):
    root = None
    yield {}, {"action": "start", "affected": []}
    for key in values:
        root, events = avl_insert(root, key)
        # ------ insertion ------
        rotation = affected = None
        for ev in events:
            if ev.get("type") == "insert":
                yield node_to_dict(root), {"action": "inserted", "key": key}
            affected = ev["affected"]
            rotation = ev["rotation"]
        # yield rotation update
        yield node_to_dict(root), {"action": "rotate", "rotation": rotation, "affected": affected}
