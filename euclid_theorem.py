#GCD of 2 numbers

def get_GCD(a, b):
	while b != 0:
		temp = a
		a = b
		b = temp % b
	return a

a = int(input()) #bigger numbers
b = int(input()) #smaller number
print(get_GCD(a, b))