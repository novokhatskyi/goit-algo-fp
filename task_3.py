from rich import print
import networkx as nx
import matplotlib.pyplot as plt
import heapq

graph_data = {
    'A': {'B': 4},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 3, 'E': 2},
    'E': {'C': 10, 'D': 2},
    'F': {'A': 7, 'D': 2}
}
G = nx.Graph()
for node in graph_data:
    for neighbor, weight in graph_data[node].items():
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

def dejkstra_algor(graph_data, start):
    distances = {node: float('inf') for node in graph_data}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        for neighbor, weight in graph_data[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


example = dejkstra_algor(graph_data, "A")

print("[bold green]Найкоротші відстані від вершини 'A':[/bold green]")
for node, dist in example.items():
    print(f"[blue]{node}[/blue]: {dist}")