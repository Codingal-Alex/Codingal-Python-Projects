
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLL:
    def __init__(self):
        self.head = None

    # Search for an element
    def searching(self, data):
        t = 0
        temp = self.head

        while temp:
            if temp.data == data:
                t = 1
                break

            temp = temp.next

        if t == 1:
            print("Element Found")
        else:
            print("Element not Found")

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

n2 = Node(8)
n1.next = n2
n2.prev = n1

n3 = Node(40)
n2.next = n3
n3.prev = n2

n4 = Node(50)
n3.next = n4
n4.prev = n3

n5 = Node(60)
n4.next = n5
n5.prev = n4

n6 = Node(70)
n5.next = n6
n6.prev = n5

n7 = Node(80)
n6.next = n7
n7.prev = n6

n8 = Node(90)
n7.next = n8
n8.prev = n7

n9 = Node(100)
n8.next = n9
n9.prev = n8

# Display the list
l.display()
print()

# Search an element
l.searching("Iamalex")
