#Calculating Power and Factorial of a number using recursion

def power(number, pow): # 5, 3
	if pow == 0:
		return 1
	else:
		return number * power(number, pow - 1)
	

def factorial(number): # 3
	if number == 0:
		return 1
	else:
		return number * factorial(number - 1)

#Test cases
print("{} power of {} is {}".format(5, 3, power(5, 3))) # 5 ^ 3 = 125
print("{} power of {} is {}".format(1, 10, power(1, 10))) # 1 ^ 10 = 1
print("Factorial of {} is {}".format(3, factorial(3))) # 3 * 2 * 1 = 6
print("Factorial of {} is {}".format(0, factorial(0))) # = 1