#Write a function to display product details by unpacking a dictionary.
#	Use unpacking to pass product details as keyword arguments to the function.

def unpacking_dictionary(**kwargs):
	return kwargs

my_dict = {"Product Name": "iPhone 15", "Price": "750$", "Memory": "128GB"}

print(unpacking_dictionary(**my_dict))
