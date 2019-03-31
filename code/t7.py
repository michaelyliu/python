try:
	f = open("file.txt")
except FileNotFoundError:
	print ("Sorry")
except Exception:
	print ("something wrong")
else: 
	print ("in else")
finally:
	print ("final act")
