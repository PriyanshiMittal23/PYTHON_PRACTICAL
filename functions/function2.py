#to count no. of vowels in a word
def count_vowels(x):
	v=0
	for i in range(len(x)):
		if x[i] in ['a','e','i','o','u','A','E','I','O','U']:
			v=v+1
	print('no. of vowels: ',v)
a=input('enter the word:')
count_vowels(a)