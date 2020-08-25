from datetime import datetime


def main():
	name = input("What is your name? ");
	bday_month = input("What month were you born in? ")

	print(f"\nHello, {name.title()}!")
	print(f"Your name has {len(name)} characters.")

	if is_current_month(bday_month):
		print("Happy Birthday Month!")


# checks if an inputed month is the current month
def is_current_month(bday_month):
	# get current date & use strftime to get the string for this month
	current_month = datetime.now().strftime("%B")

	if bday_month.lower() == current_month.lower():
		return True

	return False


if __name__ == "__main__":
	main()
