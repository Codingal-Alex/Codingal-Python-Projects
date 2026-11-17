
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

    # Search for a node
    def search(self, key):
        temp = self.head
        position = 0

        while temp is not None:
            if temp.data == key:
                print("Element found at position:", position)
                return

            temp = temp.next
            position += 1

        print("Element not found")


# Main program
ll = SinglyLL()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)

# Display linked list
print("Linked List:")
temp = ll.head

while temp:
    print(temp.data, end=" -> ")
    temp = temp.next

print("None")

# Search for an element
key = int(input("Enter the element to search: "))
ll.search(key)
