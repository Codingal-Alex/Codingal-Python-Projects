
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Address of previous node
        self.next = None  # Address of next node


class DoublyLL:
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
        new_node.prev = temp

    # Display the doubly linked list
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head

            while temp:
                print(temp.data, end=" <--> ")
                temp = temp.next

            print("None")


# Driver code
l = DoublyLL()

l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)

print("Doubly Linked List:")
l.display()
