def main():
	num_classes = int(input("How many classes are you taking? "))
	classes = get_classes(num_classes)
	print_classes(classes)


# makes a list of classes from inputed class names
def get_classes(num_classes):
	classes = []
	for i in range(num_classes):
		class_name = input(f"Enter the name of class number {i + 1}: ").title()
		classes.append(class_name)
	return classes


# prints all inputed class names
def print_classes(classes):
	print("\nThe classes you are taking are:")
	for class_name in classes:
		print(class_name)


if __name__ == "__main__":
	main()
