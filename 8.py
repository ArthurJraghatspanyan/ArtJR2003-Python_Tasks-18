#Create a function that updates user settings by passing keyword arguments dynamically.
#	Use **kwargs to accept dynamic user settings.
#	Use a function to pass these settings as keyword arguments to another function.

def user_settings_update(**kwargs):
	apply_settings(**kwargs)


def apply_settings(**user_settings):
	print(user_settings)


user_settings = {"Theme": "Dark", "Notifications": "On", "Language": "English"}

user_settings_update(**user_settings)
