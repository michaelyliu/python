#Fibonacci Generator

def fib(num):
	a, b = 0, 1
	for i in xrange(0, num):
		yield "{}:{}".format(i+1,a)
		a, b = b, a + b

for i in fib(10):
	print i