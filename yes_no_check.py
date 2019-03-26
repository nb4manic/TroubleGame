def yn_check(prompt):
	check = ''
	while True:
		check = input(prompt).strip().lower()
		if check in {'y', 'yes', 'yep'}:
			return True
		if check in {'n', 'no', 'nope'}:
			return False
		else:
			print("I'm sorry? Yes or no question, my guy. ")
			continue

    