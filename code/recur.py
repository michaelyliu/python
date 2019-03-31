

def num_ways(steps):
	if steps == 0 or steps == 1:
		return 1
	else:
		return num_ways(steps-1)+ num_ways(steps-2)

for i in range (0,10):
	print (num_ways(i))	



def num_ways_bottomup(n):
	if n == 0 or n == 1:
		return 1
	#nums = int[n+1]
	num = []
	num.append(1)
	num.append(1)
	# = 1; num[1] = 1
	for i in range (2,n):
		temp = num[i-1] + num[i-2]
		num.append(temp)
	print(num)
	return num[-1]


for i in range (1,10):
	print (num_ways_bottomup(i))	

#save space
def num_ways_bottomup_savespace(n):
	if n == 0 or n == 1:
		return 1
	num = [1,1]	
	# = 1; num[1] = 1
	for i in range (2,n):
		temp = num[0] + num[1]
		num.append(temp)
		num.pop(0)
		print(num)
	return num[-1]

for i in range (1,10):
	print (num_ways_bottomup_savespace(i))