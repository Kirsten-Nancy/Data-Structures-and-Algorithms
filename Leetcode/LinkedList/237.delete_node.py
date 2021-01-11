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


    def delete_node(self, node):
        node.data = node.next.data
        node.next = node.next.next


linked_list = LinkedList()
linked_list.head = Node(1)
node2 = Node(2)
node3 = Node(3)

linked_list.head.next = node2
node2.next = node3
linked_list.traverse()
print()
linked_list.delete_node(node2)
linked_list.traverse()