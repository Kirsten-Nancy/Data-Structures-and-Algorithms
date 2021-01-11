class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.next


    def remove_elements(self, val):
        while self.head is not None and self.head.data == val:
            self.head = self.head.next

        node = self.head

        while node is not None and node.next is not None:
            if node.next.data == val:
                node.next = node.next.next
            else:
                node = node.next
        return self.head


linked_list = LinkedList()
# Creating nodes
linked_list.head = Node(1)
node2 = Node(1)

linked_list.head.next = node2
linked_list.remove_elements(1)