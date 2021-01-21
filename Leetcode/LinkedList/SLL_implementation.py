class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next


    def append(self, val):
        """Adding a node to the end of the linked list: How? We continue traversing until we reach
        the node whose next node is None, then add the new node as the next node"""
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(val)

    def prepend(self, val):
        """Add a node to the beginning of the list"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, val):
        """Insert a node at a particular index"""
        # If a user gives an index greater than length of list, add to the end
        if index > self.length():
            self.append(val)
            return
        new_node = Node(val)
        i = 0
        current = self.head

        while i < index - 1:
            current = current.next
            i += 1
        new_node.next = current.next
        current.next = new_node

    def remove(self, index):
        """Remove a node at a particular index"""
        current = self.head
        i = 0
        while i < index - 1:
            current = current.next
        current.next = current.next.next

    def remove_head(self):
        self.head = self.head.next

    def remove_last(self):
        """Remove the last node"""
        current = self.head

        # Traverse until the second to last node
        while current.next.next:
            current = current.next
        current.next = None

    def length(self):
        """Find the length of linked list"""
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter


linked_list = LinkedList()
linked_list.head = Node(10)
linked_list.append(5)
linked_list.prepend(1)
linked_list.insert(2, 20)
print(linked_list.length())
linked_list.insert(100, 40)
linked_list.remove(1)
linked_list.remove_head()
linked_list.remove_last()
print(linked_list.head.data)
linked_list.display_list()

# TODO: Check all the possible edge cases!