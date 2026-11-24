class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert after a specific position
    def insert_after_position(self, data, position):
        temp = self.head
        count = 1

        # Find the node at the specified position
        while temp is not None and count < position:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position not found")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

    # Display the list
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Create the linked list
dll = DoublyLL()

dll.insert_beginning(10)
dll.insert_beginning(20)
dll.insert_beginning(30)

print("Original Doubly Linked List:")
dll.display()

# Insert 15 after position 2
dll.insert_after_position(15, 2)

print("\nAfter inserting 15 after position 2:")
dll.display()
