'''

PRIORITY QUEUE

in a queue, we can insert items from the back and remove items at the front

the order of elements in the queue were dictated by when items were inserted into the queue

priority queues are similar to queues except we can insert items
into the priority queue where an item has some value representing a priority 
and items are ordered in the priority queue with respect to their priority value

a heap is conceptually a complete binary tree

a binary tree is a tree where a node has at most two children

a balanced tree is a tree where the left and right subtrees of every node differ in height by no more than one

a complete tree is where every level of the tree except the deepest must contain as many nodes as possible
the deepest level must have all nodes to the left as possible

two types of heaps: maxheap, minheap

maxheap is a complete tree where the value (priority) of a node is NEVER less than the value of its children

minheap is a complete tree where the value (priority) of a node is NEVER greater than the value of its children

since binary heaps have the complete property representing this with a python list is simple:
easier to represent the heap where the 0th element in the list is meaningless
the root of the binary heap is at index 1

a node's index with respect to its parent and children can be generalized as:
a node's parent index: node_index // 2
a node's left child index: 2 * node_index 
a node's right child index: 2 * node_index + 1

insertion into a binary maxheap
insert element in the first available location (note, this will be at the end of the python list)
    keeps the binary tree complete
while the element's parent is less than the element, swap the element with its parent

removing the root element of a binary maxheap

since heaps are used to implement priority queues, removing the root element is a commonly used operation
copy the root element into a variable, assign the last_element in the python list to the root position (new_root)
while new_root is less than one of its children, swap the largest child with the new_root
return the original root element

insertion is O(log n)
deleteion is O(log n)


'''












class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0

	def percUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	def insert(self, k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)

	def percDown(self, i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp
			i = mc

	def minChild(self, i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval

bh = BinHeap()
bh.insert(5)
bh.insert(7)
bh.insert(3)
bh.insert(11)
assert bh.delMin() == 3
assert bh.delMin() == 5
assert bh.delMin() == 7
assert bh.delMin() == 11