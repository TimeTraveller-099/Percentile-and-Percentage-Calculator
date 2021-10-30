import math
print('>> To use this Program you should have Secret Code')

# Password Checker
user_attempts = 0
password = 'Raman'
turns = False

while user_attempts < 2:
	user_input = input('Enter Secret Code: ')
	if user_input == password:
		turns = True
		break
	elif user_input != password:
		print('Wrong Password!!')
		user_attempts += 1

		if user_attempts == 2:
			print('ACCESS DENIED!')
			break

# Main Program
while turns == True: 
	print('\n> What you want to calculate? (Percentage/Percentile)')
	choice = input('>> ')

	# Percentage
	if choice.lower() == 'percentage':
		print('\n__________Welcome to Percentage Calculator Machine__________\n')
		print('>> NOTE: Marks are Out of 40\n')
		print('>> Enter your Marks Below: \n')
		# Subjects Marks Input
		maths = int(input('Maths: '))
		physics = int(input('Physics: '))
		chem = int(input('Chemistry: '))
		cs = int(input('Computer Science: '))
		eng = int(input('English: '))
	
		sum = maths + physics + chem + cs + eng
		percentage = (sum/200)*100
		print('\n-->> Percentage: ', str(percentage))
		print()
		if percentage > 80:
			print(f'>> Congrats you got {percentage} percent.\n')
		elif 50 < percentage < 80:
			print(f">> You got {percentage} percent. You need some improvement.\n")
		elif 33 < percentage < 50:
			print(f">> You got {percentage} percent. You need a lot of Improvement.\n")
		elif percentage < 33:
			print(f'>> You failed in Exam, you got {percentage} percent. Work hard Next time.\n')
		

	# Percentile
	elif choice.lower() == 'percentile':
		print('\n__________Welcome to Percentile Calculator Machine__________\n')

		# Percentile = (Number of Values Below “x” / Total Number of Values) × 100
		below_user = int(input('>> No. of Students Below you: '))
		total_students = int(input('>> Total No. of Students: '))

		percentile = (below_user/total_students) * 100
		print(f"\n>> You got {percentile} percentile.")
		# Rank = ([100 - P] / 100) * N + 1
		rank = math.floor(((100 - percentile)/100) * (total_students + 1))
		print(f"\n>> You got Rank: {rank}\n")
	
	print(">>  Commands: \n  R - Restart the Program \n  E - EXIT\n")
	last = input(">> ")
	if last.lower() == 'e':
		print("----You Quit The Program----")
		break
	elif last.lower() == "r":
		continue
