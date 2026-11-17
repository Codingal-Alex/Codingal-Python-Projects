
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Address of the previous node
        self.next = None  # Address of the next node


class DoublyLL:
    def __init__(self):
        self.head = None

    # Delete node from the beginning
    def delete_beg(self):
        if self.head is not None:
            temp = self.head
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            temp = None

    # Delete node from the end
    def delete_end(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head

                while temp.next.next:
                    temp = temp.next

                temp.next = None

    # Display the linked list
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp = self.head

            while temp:
                print(temp.data, " --- >", end=" ")
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

# Delete from beginning
l.delete_beg()
l.display()
print()

# Delete from end
l.delete_end()
l.display()
