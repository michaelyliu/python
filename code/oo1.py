class Counter():
	def __init__(self, steps):
		self.steps = steps
	def num_ways(self, steps):
		if steps == 0 or steps == 1:
			return 1
		else:
			return self.num_ways(steps-1)+ self.num_ways(steps-2)

steps = 101
c = Counter(steps)

for i in range (0,20):
	print (c.num_ways(i))	
