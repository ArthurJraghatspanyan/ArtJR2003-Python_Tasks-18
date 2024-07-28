#Write a function to log messages with varying levels of severity.
#	Use *args to handle an arbitrary number of messages.
#	Use **kwargs to handle keyword arguments for metadata (like timestamp, user, etc.).

def log_messages(severity, *args, **kwargs):
	log_header = f"[{severity}]"

	if kwargs:
		metadata = " / ".join(f"{key}={value}" for key, value in kwargs.items())
		log_header += f" ({metadata})"

	for message in args:
		print(log_header, message)

log_messages("INFO", "Application started", "Initialization successful", timestamp="2024-07-26 14:00", user="admin")
log_messages("ERROR", "Failed to connect to the database", timestamp="2024-07-26 14:05")
log_messages("WARNING", "Low disk space", "Consider cleaning up old files", user="system")
