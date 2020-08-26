# from random import sample
# from string import ascii_letters, digits
# from sys import exit 
# from pprint import pprint 

# name, first_name, last_name, gmail, default_password, status, bio_data_container, container = "", "", "", "","", "", {}, {} 
# user_input = "" # stores input from users

# '''name stores the individual names of registered employee
# status holds a yes or no response from user 
# bio_data_container contains the data of each employee
# container contains the data of all registered employees 
# '''

# random_strings = "".join(sample(ascii_letters + digits,5)) # a list of random 5-character words

# print("Command-line HNG Employees Bio-data Register Application".upper().center(65, "*"))

# print()

# print("Kindly proceed to filling your bio-data.")

# print()

# def final_output():
# 	''' this prints the successfully saved bio-data of registered employees
# 	'''
# 	print("You're done saving the bio-data of HNG's employees.", "All saved data are printed below:", sep = "\n")
# 	
# 	print() 
# 	
# 	# Bio-data of all registered employees is printed
# 	pprint(container, width = 20)
# 	
# # FUNCTION DEFINITION OF MAIN()
# def main():
# 	''' this collects the bio-data of employees to be registered and saves it in a super container dictionary for each employee successfully registered
# 	'''
# 	global name, count, bio_data_container, container
# 	
# 	first_name = input("Enter your first name: ").title()
# 	
# 	while first_name.isalpha() == False or len(first_name) < 2:
# 		print()
# 		
# 		print("Invalid input!", "Name should contain only alphabets and it should have more than two characters.", sep = "\n")
# 		
# 		print()
# 		
# 		first_name = input("Enter your first name: ").title()
# 		
# 		print()
# 	
# 	last_name = input("Enter your last name: ").title()
# 	
# 	while last_name.isalpha() == False or len(last_name) < 2:
# 		print()
# 		
# 		print("Invalid input!", "Name should contain only alphabets and it should have more than two characters.", sep = "\n")
# 		
# 		print()
# 		
# 		last_name = input("Enter your last name: "). title()
# 		
# 		print()
# 		
# 	gmail = input("Enter your gmail address: ").lower()
# 	
# 	# checks for the validity of email addresses 
# 	while gmail.endswith("@gmail.com") == False or len(gmail) <= len("@gmail.com"):
# 		print()
# 		
# 		print("Invalid input!", "Enter a valid gmail address.", sep = "\n")
# 		
# 		print()
# 		
# 		gmail = input("Enter your gmail address: "). lower()
# 		
# 	default_password = first_name[:2] + last_name[-2:] + random_strings
# 	
# 	print()
# 	
# 	print(f"Your default password is {default_password}")
# 	
# 	print()
# 	
# 	print("Are you satisfied with the default password?".title())
# 	
# 	user_input = input("Enter y for 'yes' or n for 'no' please: ").lower()
# 	
# 	while user_input.isalpha() == False or user_input not in ("yes", "y", "no", "n"):
# 		print()
# 		
# 		print("Invalid input!", "Enter y for 'yes' or n for 'no' please.", sep = "\n")
# 		
# 		print()
# 		
# 		user_input = input("Enter 'y' or 'n' please: ").lower()
# 		
# 	if user_input == "no" or user_input == "n":
# 		
# 		print()
# 		
# 		default_password = input("Enter your preferred password: ")
# 		
# 		# checks for password strength
# 		while len(default_password) < 8 or default_password.isalpha() == True or default_password.isnumeric() == True or default_password[0].isupper() == False:
# 			print()
# 			
# 			print("Enter a more secure password please.","Hint: Password must start with a capital letter, it must not be less than 8 characters, it must contain numbers.",sep="\n")
# 			print()
# 			
# 			default_password = input("Enter your preferred password: ")
# 			
# 	else:
# 		pass
# 						
# 	print()
# 	
# 	name = first_name + " " + last_name 
# 	
# 	# populating sub-container
# 	bio_data_container["Full_Name"] = name
# 	bio_data_container["Email_address"] = gmail
# 	bio_data_container["Password"] = default_password
# 	
# 	# populating super-container
# 	# this prevents two registered employees having the same bio-data
# 	if bio_data_container not in container.values(): 
# 		container[name +"'s bio-data are:"] = bio_data_container
# 				
# 		print(f"{name}'s bio-data saved successfully!")
# 	
# 		print()
# 	else:
# 		print("Bio-data NOT saved since it exists!")
# 		
# 		print()
# 		
# 		next_option()
# 		
# # FUNCTION INVOCATION OF MAIN() 		
# main()

# bio_data_container = {} # this emulates the clearing of the contents of the dictionary storing the previously saved employee bio-data since this dictionary is now in a super dictionary called container & also because the empty bio_data_containerwould be used for subsequent registration of employees

# # FUNCTION DEFINITION FOR NEXT_OPTION()
# def next_option():
# 	''' this permits the registration of different employees consecutively. 
# 	'''
# 	global status, bio_data_container, user_input 
# 	
# 	print("Do you want to add another employee's bio-data?".upper())
# 	
# 	print()
# 	
# 	user_input = input("Enter y for 'yes' or n for 'no' please: ").lower()
# 		
# 	while user_input.isalpha() == False or user_input not in ("yes", "y", "no", "n"):
# 		print()
# 			
# 		print("Invalid input!", "Enter y for 'yes' or n for 'no' please.", sep = "\n")
# 			
# 		print()
# 			
# 		user_input = input("Enter 'y' or 'n' please: ").lower()
# 			
# 	if user_input == "no" or user_input == "n":
# 		status = ("no", "n")
# 		
# 		''' this is here because the execution of line 139 doesn't allow line 183 to be executed which needs to be executed for lines 189-190 and 195 to be executed consecutively. 
# 		'''
# 		if user_input in ("no", "n"):
# 			print()
# 			
# 			final_output()
# 			exit()

# 	elif user_input in ("yes", "y"):
# 		print()
# 		main() # invokes main program body
# 		bio_data_container = {} # emulates clearing of sub-container contents
# 		next_option() # recursive call that keeps asking user if he wishes to register another employee or not
# 	return status 

# # FUNCTION INVOCATION OF NEXT_OPTION()
# status = next_option()

# # this is executed when user indicates that no other employee is to registered 
# if status == ("no", "n"):
# 	pass

# print()

# # FINAL_OUTPUT INVOCATION 	
# final_output()


def sammy(a, b):
    return a+b

print(sammy(2, 3))
print()


def sam(a, b):
    return a-b

print(sam(5, 3))
print()


print("hello")