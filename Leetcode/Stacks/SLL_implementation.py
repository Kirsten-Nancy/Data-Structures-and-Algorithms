class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def push(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return self.head

        current = self.head
        new_node.next = current
        self.head = new_node
        return self.head

    def pop(self):
        removed_node = self.head
        if self.is_empty():
            return None
        # What if only the head remains
        self.head = self.head.next
        return removed_node.data

    def display_stack(self):
        current = self.head
        while current:
            print(current.data, end='-')
            current = current.next
        print()


stack = Stack()
stack.head = Node('Google')
stack.push('Udemy')
stack.push('Youtube')
stack.display_stack()
# print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.display_stack()