class stack:
	def __init__(self):
		self.l = []
	def push(self , obj):
		self.l.append(obj)
	def pop(self):
		return self.l.pop()
	def isempty(self):
		return self.l == []
	def peek (self):
		return self.l[len(self.l)-1]
	def size(self):
		return len(self.l)



	    
