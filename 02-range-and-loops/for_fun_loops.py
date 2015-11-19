# for i in range(21):
# 	if i==13:
# 		print "hello"
# 	else:
# 		print i

# for i in range(11):
# 	print i*10

# for i in range(11):
# 	if (i%2 != 0):
# 		print i


# for i in range(10,0,-1):
# 	if i==0:
# 		print "blastoff"
# 	else:
# 		print i

# fruit=["apples","oranges","bananas"]

# for l in range(3):
# 	print fruit[l]

# def sum_num(num):
# 	total=0
# 	for l in range(0,num+1):
# 		new_total=total + l
# 		total=new_total
# 		print total

# sum_num(3)

# def sum_num(num):
# 	total=0
# 	if num<=0:
# 		for l in range(num,0):
# 			new_total=total + l
# 			total=new_total
# 			print total
# 	else:
# 		for l in range(0,num):
# 			new_total=total + l
# 			total=new_total
# 			print total

# sum_num(-5)
def fizz_buzz(l):
		if (l % 3 == 0) and (l % 5==0):
			print "Fizzbuz"
		elif (l % 3 == 0):
			print "fizz"
		elif (l % 5==0):
			print "buzz"
		else:
			print l

for l in range(101):
	fizz_buzz(l)