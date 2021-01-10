class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Receives the head node
    def printList(self):
        # To indicate our first node is the head
        node = self.head
        while node is not None:
            print(node.data, end='->')
            # assign node to the next one, so: terrible explaination fyi
            node = node.next
        
        # How to add null to the end
myLinkedList = LinkedList()

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

myLinkedList.head = node1
myLinkedList.head.next = node2
node2.next = node3
node3.next = None

myLinkedList.printList()