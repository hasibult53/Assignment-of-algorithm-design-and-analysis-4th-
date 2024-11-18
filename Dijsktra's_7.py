import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # If the graph is undirected

    def dijkstra(self, start):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))  # (distance, vertex)

        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

def main():
    g = Graph()
    
    # Add edges (u, v, weight)
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    # Define the starting node directly
    start_node = 'A'
    distances = g.dijkstra(start_node)

    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")

import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # If the graph is undirected

    def dijkstra(self, start):
        priority_queue = []
        heapq.heappush(priority_queue, (0, start))  # (distance, vertex)

        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

def main():
    g = Graph()
    
    # Add edges (u, v, weight)
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    # Define the starting node directly
    start_node = 'A'
    distances = g.dijkstra(start_node)

    print("Shortest distances from node", start_node)
    for node, distance in distances.items():
        print(f"Distance to {node}: {distance}")

if __name__ == "__main__":
    main()
