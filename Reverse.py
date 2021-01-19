
def solution(N):
    enable_print = N % 10
    while N > 0:
        if enable_print == 0 and N % 10 != 0:
            enable_print = 1
        if enable_print != 0:
            print(N % 10, end='')
        N = N // 10

for x in range(20):
	solution(x)
	print('\r')
'''
if "if enable_print != 0:" be changed to "elif enable_print == 1:"
then only the ones digit equal to 1 can be printed out

'''

print('*********************')

def solution1(a):
	if int(a)<0:
		a=a[1:]
		b=-int(a[::-1])
	else:
		b=int(a[::-1])
		print(b)


for x in range(40):
	solution(x)
	print('\r')

