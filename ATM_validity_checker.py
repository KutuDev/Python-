card_digits = ""
state = False 

def ATM_validity_checker():
	'''This uses Lunh's algorithm''' 
	
	global card_digits, state
	
	while state is False:
		try:
			card_digits = input("Enter all the PAN digits located on the front of your ATM card: ")
			
			if card_digits.isdigit() is True and len(card_digits) >= 15:
				state = True
				card_digits = [int(item) for item in card_digits]
				lunh_step1a = list(map(lambda digit: (digit * 2) , card_digits[-2::-2]))
				lunh_step1b = [str(digit) for digit in lunh_step1a]
				lunh_step1ca = [list(digit) for digit in lunh_step1b]
				lunh_step1_result = sum([int(digit) for digit_string in lunh_step1ca for digit in digit_string]) 
				card_digits2 = [card_digits.remove(digit) for digit in card_digits[-2::-2]]
				lunh_step2 = sum(card_digits)
				
				lunh_ans = lunh_step1_result + lunh_step2
				
				if lunh_ans % 10 == 0:
					print("Valid")
				else:
					state = False 
					print("Invalid")
			else:
				raise ValueError 
		except ValueError:
			print()
			
			print("Invalid PAN.", "Kindly re-enter your ATM's PAN.", sep = "\n")
			
			print()	
	
ATM_validity_checker()