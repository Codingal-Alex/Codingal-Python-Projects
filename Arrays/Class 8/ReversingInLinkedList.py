
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None

    # Insert a node at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = prev

            prev = current
            current = next_node

        self.head = prev

    # Display the linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
ll = SinglyLL()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

print("Original Linked List:")
ll.display()

ll.reverse()

print("Reversed Linked List:")
ll.display()
