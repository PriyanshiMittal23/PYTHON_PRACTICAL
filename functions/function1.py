#to check if a student is present
def present(x):
	a=[12,23,61,25,42,16]
	if x in a:
		print("present")
	else:
		print("absent")
b=int(input("enter the roll no. :"))
present(b)