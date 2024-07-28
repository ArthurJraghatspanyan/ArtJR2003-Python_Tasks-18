# Create a function to greet a user with their full name and a custom message.
#	Use positional arguments for first name and last name.
# 	Use a keyword argument for the greeting message with a default value.

def greeting(name, surname, message = ''):
	full_name = f"{name} {surname}"
	print(message, full_name)


greeting("James", "Smith", message = "Welcome,")
