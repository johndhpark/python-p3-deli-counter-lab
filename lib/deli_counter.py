def line(customers):
	if len(customers) == 0:
		print("The line is currently empty.")
	else:
		print("The line is currently:", end=" ")
		for index, customer in enumerate(customers, start=1):
			delimiter = " "
			
			if index == len(customers):
				delimiter = "\n"

			print(f"{index}. {customer}", end=delimiter)


def take_a_number(deli, name):
	print(f"Welcome, {name}. You are number {len(deli) + 1} in line.")
	deli.append(name)


def now_serving(deli):
	if len(deli) == 0:
		print("There is nobody waiting to be served!")
		return

	name = deli.pop(0)
	print(f"Currently serving {name}.")