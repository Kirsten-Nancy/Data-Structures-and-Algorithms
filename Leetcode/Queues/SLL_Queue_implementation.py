class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        # Maintaining two pointers
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return 'Empty queue'
        return self.head.data

    def dequeue(self):
        if self.is_empty():
            return 'Empty queue'
        removed_node = self.head
        self.head = self.head.next
        return removed_node

    def enqueue(self, value):
        """Adding to queue given both head and tail nodes"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def enqueue_one_pointer(self, value):
        """Adding to queue given only head node"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_queue(self):
        current = self.head
        while current:
            print(current.data, end='-')
            current = current.next
        print()


queue = Queue()

queue.enqueue('Python')
queue.enqueue('Flutter')
# print(queue.peek())
queue.dequeue()
queue.display_queue()