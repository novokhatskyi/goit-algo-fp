import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq
from collections import deque


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color='white')
    plt.show()

def build_heap_tree(heap_list):
    nodes = [Node(value) for value in heap_list]
    for i in range(len(nodes)):
        left_node = 2 * i + 1     
        right_node = 2 * i + 2
        if left_node < len(nodes):
            nodes[i].left = nodes[left_node]
        if right_node < len(nodes):
            nodes[i].right = nodes[right_node]
    return nodes[0]

def bfs_visualize(root):
    queue = deque([root])
    visited = set()
    step = 0
    max_steps = count_nodes(root)  # допоміжна функція: рахує кількість вузлів

    while queue:
        node = queue.popleft()

        if node not in visited:
            # Генерую колір: наприклад, зміна інтенсивності синього
            intensity = int(255 * (step / max_steps))  # від 0 до 255
            hex_color = f'#0000{intensity:02X}'  # темно-синій до яскраво-синього

            node.color = hex_color
            visited.add(node)
            step += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def dfs_visualize(root):
    stack = [root]
    visited = set()
    step = 0
    max_steps = count_nodes(root)  # використовую ту ж функцію, що й для BFS

    while stack:
        node = stack.pop()

        if node not in visited:
            # Змінюю інтенсивність червоного кольору (від темного до яскраво-червоного)
            intensity = int(255 * (step / max_steps))
            hex_color = f'#{intensity:02X}0000'

            node.color = hex_color
            visited.add(node)
            step += 1

            # Додаю правий, потім лівий, щоб лівий оброблявся першим (як в класичному DFS)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def count_nodes(root):
    if not root:
        return 0

    count = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()
        count += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return count




if __name__ == "__main__":
    heap = [5, 7, 9, 1, 3, 8, 12, 43, 6, 4, 9, 11, 23, 17, 4]
    heapq.heapify(heap)
    root = build_heap_tree(heap)
    # bfs_visualize(root)
    dfs_visualize(root)
    draw_tree(root)