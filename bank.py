# This is a command-line banking transactions application

import stdiomask
from sys import exit

""" DECLARATION & INITIALIZATION OF  				VARIABLES
"""
prompt1, prompt2 = 0, 0  # dummy variable initialization
insecure_key = False  # variable that checks for password strength
user_balance = 5000.00
beneficiary_balance, deposit, withdraw = 0.00, 0.00, 0.00

user_email, user_password = "", ""
user_details = {}
user_input, my_input = 0, 0

# Default user details
user_details["Email address"] = "sammyjay708@gmail.com"
user_details["Password"] = "Sammyjay96"
user_details["Balance"] = user_balance

# Beneficiary email addresses
beneficiary_email = [
    "jpaul54321@gmail.com",
    "mary@gmail.com",
    "apple@gmail.com",
]

exit_kinds = ("exit", "Exit", "EXIT", "cancel", "Cancel", "CANCEL")

""" FUNCTION DEFINITIONS
"""

# The first prompt

def my_decorator(my_func):
	def exit_wrapper():
		my_func()
		 
		if (user_input or user_password or user_email) in exit_kinds:
			exit()
	return exit_wrapper

@my_decorator #this actually decorates prompt1 below	
def first_prompt():
    global prompt1, user_input 

    print("Command-line Banking Application".upper().center(65, "*"))
    
    print()
    
    print("NOTE: To terminate this application abruptly, type either 'exit' or 'cancel' anytime you're requested for an input.")
    
    print()
    
    print("You are welcome.🤝🤝🤝", "I'm here to help you with your banking transactions.", sep = "\n")

    print()

    print(
        "Choose an option below:",
        "1: Create Account",
        "2: Transactions",
        sep="\n")

    print()

    prompt1 = input("Press 1 or 2 to choose among the above listed options: ")

    # this authenticates a numeric user input only with an exception 
    if prompt1.isalpha():
        user_input = prompt1 # only the words exit, Exit, EXIT here would activate the decorator function 
    else:
        prompt1 = int(prompt1)

    print()

# Main Program Body


def main():
    if prompt1 == 1:
        create_account()
    elif prompt1 == 2:
        transactions()
    else:
        invalid_input()


def child_main():
    global prompt2, exit_kinds

    if prompt2 == 1:
        check_balance()
    elif prompt2 == 2:
        deposit()
    elif prompt2 == 3:
        withdraw()
    elif prompt2 == 4:
        transfer()
    elif prompt2 in exit_kinds:
    	pass # this allows for the execution of decorator function on transactions_child()
    else:
        child_invalid_input()

@my_decorator #this actually decorates prompt2 below
def transactions_child():
	global prompt2
    
	print(
            "Choose an option below:",
            "1: Check balance",
            "2: Deposit",
            "3: Withdraw",
            "4: Transfer",
            sep="\n")

	print()

	prompt2 = input(
            "Press 1 or 2 or 3 or 4 to choose among the above listed options: ")

	print()

        # this authenticates a numeric user input only
	if prompt2.isalpha():
		 user_input = prompt2 # only the words exit, Exit, EXIT would activate the decorator function
	else:
		prompt2 = int(prompt2)

	child_main()
	

def invalid_input():
    print("Invalid input!", "Enter either 1 or 2 please.", sep="\n")

    print()

    first_prompt()
    main()


def child_invalid_input():
    print("Invalid input!", "Enter either 1 or 2 or 3 or 4 please.", sep="\n")

    print()

    transactions()

@my_decorator #this actually decorates user_email below
def user_email_prompt():
    global user_email

    user_email = input("Type your email adress: ").lower()
    
@my_decorator #this actually decorates user_input below
def masked_password_prompt():
	global user_input
	
	user_input = stdiomask.getpass(prompt="Enter your password: ", mask = "*")
	
	print()
	 
@my_decorator #this actually decorates user_password below
def user_password_prompt():
    global user_password, insecure_key, exit_kinds  
 
    user_password = input("Enter your password: ")
	     
       # this checks for the user's password strength
    if user_password not in exit_kinds:
	    if len(user_password) < 8 or user_password.isalpha() is True or user_password.isnumeric() is True or user_password[0].isupper() == False:
	    	insecure_key = True 
	    else:
	    	insecure_key = False

# Function that creates an account for a new customer


def create_account():
    global insecure_key, user_details, user_balance, user_email

    user_email_prompt()

    print()

    # the conditional statement checks if user input email is valid in that it's length must be greater than that of "@gmail.com" and it must have
    # a suffix of "@gmail.com"
    
    # the first conditional statement below allows decorator for user_email_prompt(line 150) to work pretty well
    if user_email not in exit_kinds:
	    while user_email.endswith("@gmail.com") is False or len(user_email) <= len("@gmail.com"):
	
	        print()
	        
	        print("Invalid email address!", "Hint: use a valid gmail address.", sep="\n")
	
	        print()
	
	        user_email_prompt()
	
	    user_password_prompt()
	
	    #this prevents the acceptance of a weak password strength 
	    while insecure_key is True:
	    	
	    	print()
	    	
	    	print("Enter a more secure password please.","Hint: Password must start with a capital letter, it must not be less than 8 characters, it must contain numbers.",sep="\n")
	    	
	    	print()
	    	
	    	user_password_prompt()
	    	
	    	print()
	    
	    # new user details is stored in a dictionary data structure
	    if insecure_key is False:
	    	new_user_details = {"Email address": user_email,"Password": user_password,
	"Balance": user_balance}  
	
	    # this checks if the new user account details is not pre-existing
	    if user_details.get("Email address") != new_user_details.get("Email address") and user_details.get("Password") != new_user_details.get("Password"):
	    	
	    	print()
	    	
	    	print(f"Your account with a registered email address of {user_email} has been created with a bonus deposit of ${user_balance}!", "Proceed to performing your banking transactions of choice.", sep="\n")
	    	
	    	  # these make a new customer eligible for transactions immediately after
	        # creating an account
	    	user_details["Email Address"] = new_user_details.get("Email address")
	    	user_details["Password"] = new_user_details.get("Password")
	    	
	    	print()
	    	
	    	transactions()
	
	    else:
	    	print()
	    	
	    	print("Account creation failed!","The account details entered exists.",sep="\n")
	    	
	    	print("Kindly, re-enter a different account details.")
	    	
	    	print()
	    	
	    	create_account()

# Function that aids banking transactions

def transactions():

    global user_balance, deposit, withdraw, user_details, dummy, prompt2, user_input
    
    masked_password_prompt()

    #These conditional statements authenticates a user for transactions and permits the re-entering of password (if not recognized at first) thrice after which a new account is suggested to be created. 
    if user_input not in exit_kinds: 
	    if user_input not in user_details.values():
	    	print("Incorrect password!!!")
	    	
	    	print()
	    	
	    	print("Kindly, re-enter your password.")
	    	
	    	print()
	    	
	    	masked_password_prompt()
	    	
	    	if user_input not in user_details.values():
	    		print("Incorrect password!!!")
	    		
	    		print()
	    		
	    		print("Kindly, enter a correct password.")
	    		
	    		print()
	    		
	    		masked_password_prompt()
	    		
	    		if user_input not in user_details.values():
	    			print("Access Denied!!!", "You are an unrecognized user.", sep = "\n")
	    			
	    			print()
	    			
	    			print("Kindly proceed to creating a new account.")
	    			
	    			print()
	    			
	    			create_account()
	    		else:
	    			transactions_child()
	    	else:
	    		transactions_child()
	    else:
	        transactions_child()

def check_balance():
    global user_balance

    print(f"Your balance is ${user_balance}")
    
    print()
    
    transactions_child()


def deposit():
    global user_balance

    deposit = float(input("Enter your deposit amount: $"))
    
    print(f"You've successfully saved ${str(deposit)} into your bank account.")

    print()

    print(f"Your total balance is now ${user_balance + deposit}")
    
    print()
    
    #transactions_child()


def withdraw():
    global withdraw, user_balance

    # this ensures that withdrawal can't be done with zero available balance
    if user_balance > 0:
        withdraw = float(input("Enter your withdrawal amount: $"))

        # this prevents withdrawal greater than the available balance
        if withdraw <= user_balance:
            print()
             
            print(f"${withdraw} successfully withdrawn!")

            print()

            print(f"Your total balance is now ${user_balance - withdraw}")
        else:
            print()
            
            print(
                "Withdrawal amount is greater than available balance!",
                f"You can only withdraw an amount not greater than your available balance which is ${user_balance}",
                sep="\n")

    else:
        print() 
        
        print("Insufficient funds!!!", "Please, deposit some money.", sep="\n")

        print()

        deposit()

@my_decorator #this actually decorates recipient_email below
def transfer():
    global beneficiary_email, beneficiary_balance, user_balance, exit_kinds 

    recipient_email = input("Enter the beneficiary's email address: ")

    # this grants access to transfer to only recognized beneficiaries
    if recipient_email not in exit_kinds:
	    if recipient_email in beneficiary_email:
	        transfer_amount = float(input("Enter the amount to be transferred: $"))
	        beneficiary_balance = beneficiary_balance + transfer_amount
	
	        # this prevents the transfer of an amount greater than the available
	        # balance of user
	        if transfer_amount <= user_balance:
	
	            print()
	
	            print(
	                f"You have successfully transferred ${transfer_amount} to a beneficiary with an email address of {recipient_email}")
	
	            print()
	
	            print(f"Your total balance is now ${user_balance - transfer_amount}")
	        else:
	
	            print()
	
	            print("Insufficient funds!!!")
	    else:
	        print()
	        
	        print("Beneficiary email not recognized.")


"""MAIN FUNCTION INVOCATIONS
"""

# Function calls that starts program

first_prompt()
main()