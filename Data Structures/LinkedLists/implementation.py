class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Traversing the linked list
    def traverse_list(self):
        # To indicate our first node is the head
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
        print()

    def append_element(self, element):
        # If empty list
        if self.head is None:
            self.head = Node(element)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(element)

    def prepend_element(self, element):
        new_head = Node(element)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, element):
        while self.head is not None and self.head.data == element:
            self.head = self.head.next

        # Traverse the list starting from head
        node = self.head
        while node is not None and node.next is not None:
            if node.next.data == element:
                node.next = node.next.next
                return
            # else continue as usual to the next node
            else:
                node = node.next


linked_list = LinkedList()
# Creating nodes
linked_list.head = Node(1)
node2 = Node(1)
# node3 = Node(3)

linked_list.head.next = node2
# node2.next = node3

# Example operations
# # myLinkedList.append_element(4)
linked_list.traverse_list()
linked_list.delete_with_value(1)
linked_list.traverse_list()
# linked_list.prepend_element('new')
# linked_list.print_list()
