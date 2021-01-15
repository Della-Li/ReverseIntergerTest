


def reverseInterger(N):
	ret = 0
	while N:
		last = N%10     # Return remainder
		ret = ret*10+last
		N = N//10       # Returns the integer part of the quotient
	return ret


CyclesNumber = int(input('Please input the cycles times you like : '))

for x in range(CyclesNumber):
	N = int(input('Please input the integer which would be reversed : '))
	if N < 0:
		print('The reversed number must not less than 0')
		N = int(input('Please input the integer which would be reversed : '))
		print(N)
		print('the reversed integer is :', reverseInterger(N))
	else:
		print('the reversed integer is :', reverseInterger(N))



	

