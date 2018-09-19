graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["D"]
}


def bfs(graph, s):
    """广度优先遍历"""
    # ：params s:首节点
    queue = []
    seen = set()
    queue.append(s)
    seen.add(s)
    while len(queue) > 0:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                queue.append(i)
                seen.add(i)
        print(vertex)


def dfs(graph, s):
    """深度优先遍历"""
    # ：params s:首节点
    stack = []
    seen = set()
    stack.append(s)
    seen.add(s)
    while len(stack) > 0:
        vertex = stack.pop()
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                stack.append(i)
                seen.add(i)
        print(vertex)


dfs(graph, "A")
