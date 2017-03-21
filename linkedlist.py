class LinkedListNode(object):

	def __init__(self, val):
		self.val = val
		self.next = None

	def add(self, node):
    	current = self
		while (current.next != None):
    	current = current.next
	current.next = node

	def printList(self):
	    current = self
	while current.next != None:
	    print(current)
	print(current.val)
	current = current.next

jimmy = LinkedListNode(4)
david = LinkedListNode(2)
simon = LinkedListNode(3)

jimmy.next = david
jimmy.add(simon)
jimmy.printList()
