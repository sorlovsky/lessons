class LinkedListNode(object):

    """Docstring for LinkedListNode. """

    def __init__(self, val):
        self.val = val
        self.next = None

    def add(self, node):
        current = self
        while (current.next != None):
            current = current.next
        current.next = node 

jimmy = LinkedListNode(4)
david = LinkedListNode(2)

jimmy.add(david)
print(jimmy.next.val)


