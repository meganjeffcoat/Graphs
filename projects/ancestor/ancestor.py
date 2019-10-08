# (parent, child) pairs - set()
# individual - starting_node
# earliest - destination_node
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
    pass