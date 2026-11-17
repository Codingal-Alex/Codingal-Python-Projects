
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Address of the previous node
        self.next = None  # Address of the next node


class DoublyLL:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_beg(self, data):
        nb = Node(data)

        if self.head is not None:
            nb.next = self.head
            self.head.prev = nb

        self.head = nb

    # Insert at the end
    def insert_end(self, data):
        ne = Node(data)

        if self.head is None:
            self.head = ne
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = ne
        ne.prev = temp

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head

            while temp:
                print(temp.data, " <--> ", end="")
                temp = temp.next

            print("None")


# Driver code
l = DoublyLL()

n = Node(10)
l.head = n

n1 = Node(20)
n.next = n1
n1.prev = n

n2 = Node(30)
n1.next = n2
n2.prev = n1

# Display original list
l.display()
print()

# Insert at beginning
l.insert_beg(100)
l.display()
print()

# Insert at end
l.insert_end(100)
l.display()
