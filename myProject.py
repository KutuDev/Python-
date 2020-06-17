from datetime import datetime
from random import sample
from string import ascii_letters, digits
from pprint import pprint
from time import sleep
from sys import exit 


# placeholders used in the wild within the program body 
first_name, last_name, gmail, dept, faculty, home_address, phone_number, state_of_origin, LGA, next_of_kin_name, NoK_phone_number, matric_number, default_password, user_input, username, password, choice, bio_data_container, container, TLU = "", "","", "", "", "", "", "", "", "", "", "", "", "", "", "", "", {}, {}, 0

''' bio_data_container stores the log-in data of a registered student & container stores each registered student's bio_data_container''' 

# counter flag
count = 1

# Admin login data can be used used to login as a returning student
bio_data_container["Name"] = "Admin"
bio_data_container["Matric Number"] = "EEE/13/1107" 
bio_data_container["Password"] = "Sammyjay96"

# Admin profile data
std_name = "Admin"
dept = "Electrical/Electronics"
faculty = "Engineering" 
level = 500 
session = "2019/20" 
semester = "First" 

# Available courses for registration 
courses = ["1. \tZoology \tZOO 500 \t C \t\t3", 
		"2. \tBiology \tBIO 501 \t E \t\t1",
		"3. \tChemistry \tCHE 503 \t C \t\t1",
		"4. \tPhysics \tPHY 505 \t E \t\t2",
		"5. \tMathematics \tMAT 506 \t C \t\t3", 
]
course_units = [int(item[-1]) for item in courses]
TLU = sum(course_units)

container["Admin"] = bio_data_container 

# these are used by the ATM_validity_checker function 
card_digits, ATM_valid, state = "", False, False

# flags used in checking if some conditions are met or not
status_main, status1, status2, status3, status4, status5, status6, status7, status8, status9, status10, status11, status12, flag, flag2, flag3, flag4, ATM_flag, banner, tuition_payment_status, tuition, course_reg_status = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False 

# these gives room for the flexibility of phone numbers across countries 
zip_code = "+234"
dummy_phone_number = "+2349016012789"

# a list of random 5-character words
random_strings = "".join(sample(ascii_letters + digits,5)) 

'''FIRST-PROMPT''' 
print("Command-line Student Management System".upper().center(65, "*"))

print()

print("Courtesy: John Samuel (Scholar Network Python Bootcamp 2020)".title().center(65, "-"))

print()

print("You are welcome.", 
		"I'm here to help you with your online portal creation and course registration.", 
		sep = "\n")

print()


def main():
	''' This is the homepage where a user chooses a preferred option. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global status_main, status1 

	print(
	        "Choose an option below:", 
	        "1: New student",
	        "2: Returning student",
	        "3: Exit", 
	        sep="\n")
	
	print()
	
	while status_main is False:
		try:
			prompt1 = int(input("Enter 1 or 2 or 3 to choose among the above listed options: ")) 
			
			if prompt1 == 1:
				status_main = True
				status1 = False 
				
				print()
				
				create_account()
				
				print()
				
				print("Kindly proceed to your online portal.")
				
				online_portal()
				
				print()
				
			elif prompt1 == 2:
				status_main = True 
				
				online_portal()
				
			elif prompt1 == 3:
				print()
				print(f"Goodbye {std_name}....................")
				exit()
			else:
				raise ValueError 
		except ValueError:
			print()
			
			print("Invalid input!", 
					"Enter either 1 or 2 please.", 
					sep = "\n")
					
			print()
			
def create_account():
	''' This creates an online portal account for a new student. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	global status_main, status1, status2, status3, status4, status5, status6, status7, status8, status9, status10, status11, status12, count, flag, first_name, last_name, gmail, std_name, dept, level, faculty, home_address, phone_number, state_of_origin, LGA, next_of_kin_name, NoK_phone_number, matric_number, default_password, name, count, bio_data_container, container
	
	print("Registration page".title().center(65, "-"))
	
	print()
	
	print("Kindly enter your bio-data as follows:")
	
	print()
	
	# this ensures that the prompt that ask if newly registered student want to proceed to the online portal is activated
	flag = False 
	
	# this ensures that the student's first name contains only alphabets & that it has more than two letters
	while status1 is False: 
		try: 
			first_name = input("Enter your first name: ").title()
			
			if (first_name.isalpha() is False and "-" not in first_name) or first_name.isdigit() is True or len(first_name) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status1 = True
		except ValueError:
				print("Invalid first name!", 
			"Kindly enter a valid first name.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's last name contains only alphabets & that it has more than two letters
	while status2 is False: 
		try: 
			last_name = input("Enter your last name: ").title()
			
			if (last_name.isalpha() is False and "-" not in last_name) or last_name.isdigit() is True or len(last_name) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status2 = True
		except ValueError:
				print("Invalid last name!", 
			"Kindly enter a valid last name.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's gmail address is valid & that it has more than ten characters 
	while status3 is False: 
		try: 
			gmail = input("Enter your email address: ").lower()
			
			if (gmail.endswith("@gmail.com") is False and gmail.endswith("@ymail.com") is False) or len(gmail) <= len("@gmail.com"):
				print()
			
				raise ValueError 
			
				print()
			else:
				status3 = True
		except ValueError:
				print("Invalid email address!", 
			"Kindly enter a valid gmail address.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's department contains only a mix of alphabets & characters and that it has more than two characters 
	while status4 is False: 
		try: 
			dept = input("Enter your department/course of study: ").title()
			
			if (dept.isalnum() is True and dept.isalpha() is False) or len(dept) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status4 = True
		except ValueError:
				print("Invalid name input!", 
			"Kindly enter a valid name for your course of study.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's faculty contains only a mix of alphabets & characters and that it has more than two characters 
	while status5 is False: 
		try: 
			faculty = input("Enter the name of your faculty: ").title()
			
			if (faculty.isalnum() is True and faculty.isalpha() is False) or len(faculty) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status5 = True
		except ValueError:
				print("Invalid name input!", 
			"Kindly enter a valid name for your faculty.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's home address contains only a mix of alphabets & characters and that it has more than two characters 
	while status6 is False: 
		try: 
			home_address = input("Enter your residential address: ").capitalize()
			
			if home_address.isdigit() is True or len(home_address) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status6 = True
		except ValueError:
				print("Invalid residential address!", 
			"Kindly enter a valid residential address address.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's phone number is valid and that it has a valid length. 
	while status7 is False: 
		try: 
			phone_number = input("Enter your telephone number prefixed with your country's zip code: ")
			
			if phone_number.startswith(zip_code) is False or len(phone_number) != len(dummy_phone_number):
				print()
			
				raise ValueError 
			
				print()
			else:
				status7 = True
		except ValueError:
				print("Invalid phone number!", 
			"Kindly enter a valid phone number.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's state of origin contains only alphabets and that it has more than two characters 
	while status8 is False: 
		try: 
			state_of_origin = input("Enter your state of origin: ").capitalize()
			
			if state_of_origin.isalpha() is False or len(state_of_origin) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status8 = True
		except ValueError:
				print("Invalid state of origin!", 
			"Kindly enter a valid state of origin.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's LGA contains only alphabets and that it has more than two characters 
	while status9 is False: 
		try: 
			LGA = input("Enter your Local Government Area: ").capitalize()
			
			if LGA.isalpha() is False or len(LGA) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status9 = True
		except ValueError:
				print("Invalid LGA!", 
			"Kindly enter a valid Local Government Area.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's next of Kin's name contains only a mix of alphabets & characters and that it has more than two characters 
	while status10 is False: 
		try: 
			next_of_kin_name = input("Enter the full name of your Next of Kin: ").title()
			
			if next_of_kin_name.isalnum() is True and next_of_kin_name.isalpha() is False or len(next_of_kin_name) < 2:
				print()
			
				raise ValueError 
			
				print()
			else:
				status10 = True
		except ValueError:
				print("Invalid name input!", 
			"Kindly enter a valid name for your Next of Kin.", 
			sep = "\n")
			
				print()
				
	# this ensures that the student's next of Kin's phone number is valid and that it has a valid length
	while status11 is False: 
		try: 
			NoK_phone_number = input("Enter your Next of Kin's telephone number prefixed with your country's zip code: ")
			
			if NoK_phone_number.startswith(zip_code) is False or len(NoK_phone_number) != len(dummy_phone_number):
				print()
			
				raise ValueError 
			
				print()
			else:
				status11 = True
		except ValueError:
				print("Invalid phone number!", 
			"Kindly enter a valid phone number for your Next of Kin.", 
			sep = "\n")
			
				print()
				
	''' the below generates student's matric number automatically using the format: 
ELE/20/0001 <> {first three letters of student's department}/{last two digits of current year of registration}/{random 4 digits incremented per registered student} 
	'''
	today = datetime.today()
	last_digits = "{:0>4}".format(count)
	count += 1 # this makes the last four digits in matric number to be incremented for each newly registered student 
	matric_number = dept[:3].upper() + "/" + today.strftime("%y") + "/" + last_digits
	
	print()
	 
	''' the below generates a default password automatically using the format: 
Sajnjay96 <> {first two letters of student's first name(first letter is capitalized)}/{last two letters of student's last name}/{random 5-character word} 
	''' 
	default_password = first_name[:2] + last_name[-2:] + random_strings
	
	print()
	
	print(f"Your default password is {default_password}")
	
	print()
	
	print("Are you satisfied with the default password?".title())
	
	print()
	
	# these allows the new student to be able to create their preferred password 
	while status12 is False:
		try:
			user_input = input("Enter y for 'yes' or n for 'no' please: ").lower()
			
			if user_input not in ("yes", "y", "no", "n"):
				raise ValueError 
			else:
				status12 = True
		except ValueError:
			print("Invalid input!", 
				"Kindly enter y for 'yes' or n for 'no' please.", 
				sep = "\n")
				
			print()
			
	if user_input == "no" or user_input == "n":
		
		print()
		
		default_password = input("Enter your preferred password: ")
		
		# checks for password strength
		while len(default_password) < 8 or default_password.isalpha() == True or default_password.isnumeric() == True or default_password[0].isupper() == False:
			print()
			
			print("Enter a more secure password please.","Hint: Password must start with a capital letter, it must not be less than 8 characters, it must contain numbers.",sep="\n")
			print()
			
			default_password = input("Enter your preferred password: ")
			
	else:
		pass
						
	print()
	
	# these overwrites admin's info with new student's own
	std_name = first_name + " " + last_name 
	dept = dept
	faculty = faculty 
	level = 100 
	session = str(int(today.strftime("%Y"))-1) + "/" + today.strftime("%y") # creates 2019/20 session format 
	semester = "First" 
	
	# this populates a dictionary with log in details of newly registered student
	bio_data_container["Name"] = std_name
	bio_data_container["Matric Number"] = matric_number
	bio_data_container["Password"] = default_password
	
	print("Online portal registration successful!")
	
	print()
	
	print("Your log-in details are:")
	
	pprint(bio_data_container, width = 20)
	
	print()
	
	print("Would you like to proceed over to your online portal?")
	
	print()
	
	# these allows newly registered student to proceed to log in to the online portal 
	while flag is False:
		try:
			ext_input = input("Enter y for 'yes' or n for 'no' to go back to the previous page: ").lower()
			
			if ext_input in ("yes", "y"):
				flag = True
				online_portal()
			elif ext_input in ("no", "n"):
				
				# Reset flags to allow for multiple registration of new students 
				status_main, status1, status2, status3, status4, status5, status6, status7, status8, status9, status10, status11, status12, flag, flag2, flag3, flag4, ATM_flag, banner, tuition_payment_status, tuition, course_reg_status = False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False 
				flag = True
				status_main = False
				print()
				main()
			else:
				raise ValueError 
		except ValueError:
			print()
			
			print("Invalid input!", "Enter y for 'yes' or n for 'no'.")
	
	
def online_portal():
	''' This grants access to the online portal after a successful log in. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		N/A
		
	'''
	
	login_page()
	
	
def login_data():
	''' This accepts log in information of students. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		N/A
		
	'''
	
	global username, password
	 
	username = input("Enter your matric number: ").upper()
	password = input("Enter your password: ")
	
	
def login_page():
	''' This is the page opened after a successful log in by student. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global bio_data_container, status_main, tuition, banner, flag, flag2, flag3, flag4, ATM_flag, banner, tuition_payment_status, tuition, course_reg_status
	
	print()
	
	print("Student login page".title().center(65, "-"))
	
	print()
	
	print("Kindly enter your log-in information as follows:")
	
	print()
	
	login_data()
	
	print()
	
	print("-" * 65)
	
	print()
	
	# grants access to only registered student
	if username == bio_data_container.get("Matric Number") and password == bio_data_container.get("Password"):
		
		# Resets all flags used outside the create_account function 
		flag, flag2, flag3, flag4, ATM_flag, banner, tuition_payment_status, tuition, course_reg_status = False, False, False, False, False, False, False, False, False 
		 
		child_login_page()
		
	else:
		status_main = False
		
		print()
		
		print("Incorrect data!!!", "Redirecting to main menu.....  .....  ......  ...... ", sep = "\n")
		
		sleep(1)
		
		print()
			
		main()


def student_profile():
	''' This displays some bio-data information about logged in student. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		N/A
		
	'''
	
	print(f"Name: {std_name}", 
			f"Department: {dept}", 
			f"Faculty: {faculty}", 
			f"Level: {level}", 
			f"Session: {session}", 
			f"Semester: {semester}", 
			sep = "\n")


def child_login_page():
	''' This opens up a page where a logged in student can choose his preferred action. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global flag2, status_main, std_name, tuition_payment_status, ATM_flag, state, banner
	
	print()
		
	print("Welcome back {},".format(bio_data_container.get("Name")))
		
	print()
		
	print("{}'s profile".format(bio_data_container.get("Name")).center(65, "-"))
	
	print()
		
	student_profile()
		
	print("-"*65)
		
	print()
	
	print(
	        "Choose an option below:", 
	        "1: Pay tuition",
	        "2: Course registration",
	        "3: Logout", 
	        sep="\n")
	        
	print()
		
	# these allows newly registered student to proceed to log in to the tuition payment page
	while flag2 is False:
		print("To be enabled for your course registration, you need to pay your tuition fees, would you like to proceed over to paying your tuition now?")
		
		print()
		try:
			pay_tuition_input = int(input("Enter 1 or 2 or 3: ")) 
				
			if pay_tuition_input == 1:
				flag2 = True
				ATM_flag = True
				state = False 
				tuition_payment()
			elif pay_tuition_input == 2:
				banner = False 
				flag2 = True 
				course_reg_form()
			elif pay_tuition_input == 3:
				flag2 = True
				status_main = False
				print()
				print("Re-directing back to the main menu......  ......  ...  ..... ")
				sleep(2)
				print()
				main()
			else:
				raise ValueError 
		except ValueError:
			flag2 = False 
			print()
				
			print("Invalid input!")
			
			print()
			
			child_login_page()
	
			
def child_ATM_validity_checker():
	''' This allows multiple trials of PAN input if invalid at previous check. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global ATM_flag, state, flag2
	
	print("Would you like to try again?")
	
	while ATM_flag is False:
		try:
			print()
			intake = input("Enter y for 'yes' or n for 'no' to return to the student profile page: ").lower()
			print()
			if intake in ("yes", "y"):
				ATM_flag = True
				state = False
				ATM_validity_checker()
			elif intake in ("no", "n"): 
				flag2 = False 
				child_login_page()
			else:
				raise ValueError 
		except ValueError:
			print()
			print("Invalid input!", "Enter y for 'yes' or n for 'no'.")
	

def ATM_validity_checker():
	''' This uses Lunh's algorithm to validate an ATM card required for tuition payment by performing some calculations on the 15/16 long PAN digits on the front of the card.
			
	Args:
		N/A
	
	Returns:
		ATM_valid boolean state
		
	Raises:
		ValueError: if  user_input is incorrect 
	
	The variables lunh_step1a, lunh_step1b, lunh_step1c, lunh_step1_result, lunh_step2, lunh_ans are the results of the 3 action steps in Lunh's algorithm:
		
		step 1- starting from the penultimate digit (down to the first digit) multiply every second-placed digit by 2, then add all the individual digit found in the result obtained earlier together. 
		step 2- add the total sum obtained above to the sum of all PAN digits not multiplied by 2 in the above step.
		step 3- The ATM card is valid if the remainder of the division of the result obtained above by 10 is 0.
	''' 
	
	global card_digits, state, ATM_valid, ATM_flag, flag2
	
	while state is False:
		try:
			card_digits = input("Enter all the 15 or 16-digits long PAN located on the front of your ATM card: ")
			
			# deployment of Lunh's algorithm 
			if card_digits.isdigit() is True and len(card_digits) >= 15:
				state = True
				card_digits = [int(item) for item in card_digits]
				lunh_step1a = list(map(lambda digit: (digit * 2) , card_digits[-2::-2]))
				lunh_step1b = [str(digit) for digit in lunh_step1a]
				lunh_step1c = [list(digit) for digit in lunh_step1b]
				lunh_step1_result = sum([int(digit) for digit_string in lunh_step1c for digit in digit_string]) 
				card_digits2 = [card_digits.remove(digit) for digit in card_digits[-2::-2]]
				lunh_step2 = sum(card_digits)
				
				lunh_ans = lunh_step1_result + lunh_step2
				
				print() 
				
				print()
				
				print("Checking the validity of your ATM card... .....  .....  ....  .....")
					
				print()
			
				print("Please wait a bit.")
					
				print()
					
				sleep(3)
				
				if lunh_ans % 10 == 0:
					print("ATM card is Valid!")
					ATM_valid = True 
				else:
					ATM_flag = False
					print("Invalid ATM card!!!")
					print()
					child_ATM_validity_checker()
			else:
				ATM_flag = False
				state = True
				print()
				print("Invalid PAN.", "Kindly re-enter your ATM's PAN.", sep = "\n")
				print()
				child_ATM_validity_checker() 
		except ValueError:
			print()
			
			print("Invalid PAN.", "Kindly re-enter your ATM's PAN.", sep = "\n")
			
			print()
	return ATM_valid 	

def child_menu_options():
	''' This page is opened after a successful tuition payment wherein the student can choose his/her preferred next choice of action.
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global flag2, flag3, banner
	
	print(
	        "Choose an option below:", 
	        "1: Course registration",
	        "2: Student profile",
	        sep="\n")
	        
	print()
		
	print("You are cleared for your course registration.")
		
	print()
		
	# these allows newly registered student to proceed to the course registration page
	while flag3 is False:
		try:
			course_reg_input = int(input("Enter 1 or 2 to choose among the above listed options: ")) 
				
			if course_reg_input == 1:
				banner = False 
				flag3 = True
					
				print()
					
				print("Please wait a bit..... .... ... .. .")
					
				print()
					
				sleep(3)
				course_reg_form()
			elif course_reg_input == 2:
				flag2 = False 
				flag3 = True
				banner = False 
				child_login_page()
			else:
				raise ValueError 
		except ValueError:
			print()
				
			print("Invalid input!")
			
	
def tuition_payment():
	''' This opens the tuition payment platform. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global tuition_payment_status, flag2, flag3, tuition, bio_data_container, course_reg_status, state 
	
	print()
	
	print("Tuition payment".center(65, "-"))
	
	print()
	
	# Admin need not pay tuition 
	if bio_data_container.get("Matric Number") == "EEE/13/1107" and bio_data_container.get("Password") == "Sammyjay96":
		tuition = True
		course_reg_status = True
		
	if tuition is False:
		state == False 
		tuition_payment_status = ATM_validity_checker()
	else:
		flag3 = False 
		print("You've paid tuition before.")
		print("-" * 65)
		
		print()
		
		child_menu_options()
	
	print()
	
	# access to course registration is granted only to students who have paid their tuition. 
	if tuition_payment_status:
		flag3 = False 
		tuition = True 
		print("Tuition successfully paid.")
		
		print()
		
		print("-" * 65)
		
		print()
		
		print("Re-directing a step backwards......  ......  ...  ..... ")
		
		sleep(2)
		
		print()
		
		child_menu_options()
		
		
def course_reg_form():
	''' This opens the course registration page only for students who have paid their tuition. 
	
	Args:
		N/A
	
	Returns:
		N/A
		
	Raises:
		ValueError: if  user_input is incorrect
		
	'''
	
	global banner, choice, TLU, flag2, flag4, status_main, tuition, bio_data_container, course_reg_status, banner 
	
	print()
	
	# Admin need not pay tuition to register courses
	if bio_data_container.get("Matric Number") == "EEE/13/1107" and bio_data_container.get("Password") == "Sammyjay96":
		tuition = True 
		course_reg_status = True
	
	if tuition_payment_status is True or tuition is True:
		
		if course_reg_status is True:
			print("You've done your course registration before.")
			banner = True
			flag2 = False
			flag4 = True
			print()
			print("Redirecting to the student profile page......   .......   ........ ")
			print()
			sleep(3)
			child_login_page()
			print()
			print()	
		else:
			print("Course registration page".center(65, "-"))
			print()
			
			print(f"{std_name}, the following are the courses available for registration.")
			
			print()
		
		# these prints the information about the available courses for registration in a tabular form
			print("\tName \t\tCourse code \t Status \tUnits")
			for item in courses:
				print(item)
				
			print()
			
			print("Would you like to register the courses listed above?")
		
			print()
	
		# these allows newly registered student to proceed to log in to the online portal 
		while banner is False:
			try:
				choice = input("Enter y for 'yes' or n for 'no' to go back to the student profile page: ").lower()
				
				print()
				
				if choice in ("yes", "y") and course_reg_status is False:
					banner = True
					flag4 = True
					flag2 = False
					print(f"Course registration successful with {TLU} total load units!")
					print()
					print("Re-directing back to the student profile page......  ....  ....   ..... .. ")
					sleep(3)
					print()
					child_login_page()
					
				elif choice in ("yes", "y") and course_reg_status is True:
					print("You've done your course registration before.")
					banner = True
					flag4 = True
					flag2 = False
					print()
					print("Redirecting to the student profile page......   .......   ........ ")
					print()
					sleep(3)
					child_login_page()
					print()
				elif choice in ("no", "n"):
					banner = True
					flag2 = False 
					child_login_page()
				else:
					raise ValueError 
			except ValueError:
				print()
				
				print("Invalid input!", "Enter y for 'yes' or n for 'no'.")
	else:
		print("Access denied!!!")
		
		print()
		
		print("Kindly pay your tuition in order to be allowed to register your courses.")
		
		print()
		
		print("Would you like to pay your tuition now?")
		
		print()
		
		# these allow logged in student to be redirected to tuition payment page or login page
		while flag4 is False:
			try:
				back_choice = input("Enter y for 'yes' or n for 'no' to be redirected to the student profile page: ").lower()
				
				print()
				
				if back_choice in ("yes", "y"):
					flag4 = True
					tuition_payment()
				elif back_choice in ("no", "n"):
					flag4 = True
					flag2 = False
					child_login_page()
				else:
					raise ValueError 
			except ValueError:
				print()
				
				print("Invalid input!", "Enter y for 'yes' or n for 'no'.")
				
				print()

# MAIN PROGRAM INVOCATION 	
main()