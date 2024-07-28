#Create a function to print a user profile.
#	Use keyword-only arguments for age and city.
#	Use positional arguments for first name and last name. (print_user_profile("John", "Doe", age=30, city="New York")
#	Return the result of the operation.

def user_profile(name, surname, age = 30, city = "New York"):
	return f"User profile is: Name: {name}, Surname: {surname}, Age: {age}, City: {city}"

result1 = user_profile("John", "Doe")
print(result1)

result2 = user_profile("Bob", "Smith", 25, "Los Angeles")
print(result2)
