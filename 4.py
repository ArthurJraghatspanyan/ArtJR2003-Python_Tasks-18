#Write a function to process data with different operations.
#	Use positional-only arguments for data (list of numbers).
#	Use a keyword argument for the operation (default is ‘sum’).
#	Return the result of the operation.

def different_operations_for_data(data, /, operation = 'sum'):
	summary = 0
	subtract = 0
	multiply = 1
	for i in data:
		if operation == 'sum':
			summary += i
			return summary
		elif operation == '-':
			subtract -= i
			return subtract
		elif operation == '*':
			multiply *= i
			return multiply
		else:
			return "Sorry, other operation are not supportable yet. This is alpha version :)"

ls = [1, 2, 3, 4, 5]

result1 = different_operations_for_data(ls)
print(result1)

result2 = different_operations_for_data(ls, operation = '-')
print(result2)

result3 = different_operations_for_data(ls, operation = '*')
print(result3)
