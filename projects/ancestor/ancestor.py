# (parent, child) pairs - set()
# individual - starting_vertex
# earliest - destination_vertex
# farthest distance from the input individual - path
# -1 if no parents
# ancestors - vertex
# parent - edges?
# use a cache?


class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    graph = {}
    for pair in ancestors:
        if pair[1] in graph:
            graph[pair[1]].append(pair[0])
        else:
            graph[pair[1]] = [pair[0]]
        
    stack = Stack()
    result = starting_node
    visited = set()
    stack.push([starting_node])
    a_len = 0

    if starting_node not in graph:
        return -1
    while stack.size() > 0:
        path = stack.pop()
        node = path[-1]
        if node in graph:
            for parent in graph[node]:
                new_path = list(path)
                new_path.append(parent)
                stack.push(new_path)
                if new_path == 0:
                    result = min(result, parent)
                elif len(new_path) > a_len:
                    result = parent
                    a_len = len(new_path)
    return result

    