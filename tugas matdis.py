#Asti Oktapianti
#F1E125072
#Sistem Informasi R001

import heapq

# Graph hasil pembacaan dari gambar yang telah dibuat
graph = {
    'a': {'b': 38, 'e': 178},
    'b': {'a': 38, 'f': 47, 'c': 202},
    'c': {'b': 202, 'd': 40, 'p': 39},
    'd': {'c': 40, 'q': 105},
    'e': {'a': 178, 'i': 35},
    'f': {'b': 47, 'g': 43, 'j': 71},
    'g': {'f': 43, 'h': 44, 'k': 57},
    'h': {'g': 44, 'i': 42, 'l': 38},
    'i': {'h': 42, 'e': 35, 'm': 24},
    'j': {'f': 71, 'p': 101, 'k': 40},
    'k': {'j': 40, 'l': 39, 'o': 84, 'g': 57},
    'l': {'k': 39, 'm': 27, 'h': 38, 'n':68 },
    'm': {'l': 27, 'i': 24, 'n': 66},
    'n': {'m': 66, 'q': 58, 'n': 68},
    'o': {'p': 44, 'k': 84},
    'p': {'c': 39, 'o': 44, 'j': 101},
    'q': {'d': 105, 'n': 58}
}

def dijkstra(graph, start, target):
    # priority queue
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        path = path + [node]

        # jika sudah sampai tujuan
        if node == target:
            return cost, path

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return float("inf"), []

# Jalankan
distance, path = dijkstra(graph, 'a', 'q')

print("Jarak Terpendek:", distance)
print("Jalur:", " -> ".join(path))
