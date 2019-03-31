test = {1, 3, 5}
#print (test)


def num_ways_x(n):

	if n == 0: 
		return 1
	total = 0
	for i in [1, 3, 5]:
		if n - i >= 0: 
			total += num_ways_x(n-i)
			#print (total)
  
	return total
	


print(num_ways_x(6))		
