for num in xrange (1,100):
	if num % 5 == 0 and num %3 == 0:
		print "fizzbuzz"
	elif num % 5 == 0:
		print "fizz"
	elif num % 3 == 0:
		print "buzz"
	else:
		print num

a, b = 0, 1

for x in xrange(1,10):
	print a
	a, b = b, a + b



