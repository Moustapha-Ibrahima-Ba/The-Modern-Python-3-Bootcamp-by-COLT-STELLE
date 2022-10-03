# ask for age
# age = input("How old are you ? \n")

# if age:

# 	age = int(age)
# 	if age >= 18 and age < 21:
# 		# 18-21 wristbrand
# 		print("You can enter, but need a wristbrand")

# 	elif age >= 21:
# 		# 21+ drink, normal entry
# 		print("You are good to enter and can drink!")

# 	else:
# 		# too young, sorry 
# 		print("You can't come in, little one")
# else:
# 	print("Please enter an age!")


# ask for age
age = input("How old are you ? \n")

if age:

	age = int(age)

	if age >= 21:
		# 21+ drink, normal entry
		print("You are good to enter and can drink!")

	elif age >= 18:
		# 18-21 wristbrand
		print("You can enter, but need a wristbrand")


	else:
		# too young, sorry 
		print("You can't come in, little one")
else:
	print("Please enter an age!")