## Algorithms course 1, assignment 1
## Karatsuba multiplication problem using recursion

def karatsuba(x,y):
	


	if x < 10 and y < 10:
		return x * y

	if x >= y:
		num1 = str(x)
		num2 = str(y)
	else:
		num1 = str(y)
		num2 = str(x)	

	n = len(num1) - 1
	m = len(num2) - 1

	if n > m:
		dn = n-m
		num2 = '0'*dn + num2

	a = num1[0]
	b = num1[1:]
	c = num2[0]
	d = num2[1:]

	if len(b) == 0:
		b = str(0)
	if len(d) == 0:
		d = str(0)	

	## step 1
	d1 = int(a) * int(c)

	## step 2
	if int(b) == 0 or int(d) == 0:
		d3 = 0
	elif int(b) < 10 and int(d) < 10:
		d3 = int(b) * int(d)
	else:
		d3 = karatsuba(int(b), int(d))

	## step 3
	c1 = str(int(a) + int(b))
	c2 = str(int(c) + int(d))

	## step 4
	if len(c1) == 0 or len(c2) == 0:
		c3 = 0
	elif int(c1) < 10 and int(c2) < 10:
		c3 = int(c1) * int(c2)
	else:
		c3 = karatsuba(int(c1), int(c2))

	d2 = str(int(c3) - int(d1) - int(d3))
	final = str((int(d1) * 10**(n + m)) + (10**(n) * int(d2)) + int(d3))
	
	return final


xx = int(3141592653589793238462643383279502884197169399375105820974944592)
yy = int(2718281828459045235360287471352662497757247093699959574966967627)

#xx = int(31415926348373343543112256773)
#yy = int(27182818028475236567725234566)
#xx = int(1456)
#yy = int(1256)

print(xx)
print(yy)

ans = karatsuba(xx,yy)
print(ans)


## Answer from regular multiplication
print("multiplied = ")
print(xx*yy)