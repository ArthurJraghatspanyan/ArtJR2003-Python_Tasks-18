#Create a function to generate a report with both required and optional sections.
#	Use positional arguments for required sections.
#	Use keyword arguments for optional sections with default values.

def report_message(report, message, /, grows = None, conclusion = None):
	report = f"Report theme: {report}\nMessage: {message}\n"

	if grows:
		report += f"Grows: {grows}\n"

	if conclusion:
		report += f"Conclusion: {conclusion}"

	return report

report = report_message("Employers Punctuality Report", "This report shows the company's employers' punctuality.", grows = "Our employerss punctuality is always on high level.", conclusion = "The company had a successful year.")
print(report)
