import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    previous_nodes = {node: None for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            break
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1]
    
    return distances, path

# Definisikan graph berdasarkan soal
graph = {
    'A': {'B': 6, 'C': 4},
    'B': {'H': 8},
    'C': {'D': 6, 'E': 7},
    'D': {'G': 5, 'F': 6},
    'E': {'I': 12},
    'F': {'H': 2},
    'G': {'I': 7},
    'H': {'I': 7},
    'I': {}
}

# Cari jalur terpendek dari A ke I
distances, path = dijkstra(graph, 'A', 'I')
print(f"Jarak terpendek dari A ke I adalah {distances['I']} km")
print(f"Rute tercepat sesuai perhitungan adalah {' -> '.join(path)}")

# Visualisasi graph
G = nx.Graph()

# Tambahkan semua edges ke graph
for node, edges in graph.items():
    for neighbor, weight in edges.items():
        G.add_edge(node, neighbor, weight=weight)

# Gambar graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Graph Jarak")
plt.show()
