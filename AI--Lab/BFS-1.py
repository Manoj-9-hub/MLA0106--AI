from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F','G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = set()
queue = deque(['A'])

visited.add('A')

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for n in graph[node]:
        if n not in visited:
            visited.add(n)
            queue.append(n)