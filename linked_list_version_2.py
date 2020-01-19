#learning linked list

#node class
class Node(object):
	def __init__(self,val): #constructor
		self.val = val
		self.next = None

	def get_data(self): #returns the value of the node
		return self.val

	def set_data(self, val): #set the value of the node
		self.val = val

	def get_next(self): #get the next node
		return self.next

	def set_next(self, next): #set the next node
		self.next = next

class Linked_list(object):#linked list class
	def __init__(self, head = None):
		self.head = head
		self.count = 0

	def get_count(self):
		return self.count

	def insert(self, data): #insert a new node
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node
		self.count += 1

	def find(self, val): #find a first item with the given value(val)
		item = self.head
		while(item != None):
			if item.get_data() == val:
				return item
			else:
				item = item.get_next()
		return None

	def delete(self, index): #delete the node at a given index and adjust the next and head
		if index > self.count - 1:
			return
		if index == 0:
			self.head = self.head.get_next()
		else:
			temp_index = 0
			node = self.head
			while temp_index < index - 1:
				node = node.get_next()
				temp_index += 1
			node.set_next(node.get_next().get_next())
			self.count -= 1

#create a linkedlist and add some items
itemList = Linked_list()
itemList.insert(20)
itemList.insert(30)
itemList.insert(40)
itemList.insert(50)
itemList.insert(60)

print("Learning Linked List")

#operations on linked list
print("Item count", itemList.get_count())
print("Finding item", itemList.find(20)) #true
print("Finding item", itemList.find(10)) #false


#delete nodes
itemList.delete(3)
print("Item count", itemList.get_count())
print("Finding item", itemList.find(30)) #true