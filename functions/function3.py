#to print factorial of a no.
def fact(x):
	a=1
	while(x!=0):
		a=a*x
		x=x-1
	print('factorial:',a)
a=int(input('enter the no.'))
fact(a)