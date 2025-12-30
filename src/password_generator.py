import string
from random import *
from loading_effect import *
from mahoa import *


def generation():

	Alphabet_letter = list(string.ascii_letters)

	Alphabet_digits = list(string.digits)
	Alphabet_punctuation = list(string.punctuation)

	Alphabet_letter.extend(Alphabet_digits)
	Alphabet_letter.extend(Alphabet_punctuation)

	Pass_list = []
	print("Recommended: >= 10 characters")
	choose = input("Lenghth (Enter = Random): ")
	if choose == "":
		r_dom = random.randint(10, 20)
		for element in range(0, r_dom):
			Pass_list.append(random.choice(Alphabet_letter))
		pre_effect(r_dom)

	elif choose.isnumeric():
		choose = int(choose)
		
		for element in range(0, choose):
			Pass_list.append(random.choice(Alphabet_letter))
		pre_effect(choose)
	
	result = ""
	for element in Pass_list:
		result += element
		
		
	sys.stdout.flush()

	sys.stdout.write("\r")
	sys.stdout.write("Password: " + result + "                                ")
	print("\nMã hóa: " ,mahoa(result))
	

	
def edit():
	Alphabet_digits = list(string.digits)
	Alphabet_punctuation = list(string.punctuation)
	Alphabet_digits.extend(Alphabet_punctuation)

	user_pass = input("Password: ")
	convert_list = []
	convert_list[:0] = user_pass
	first_pos = []
	last_pos = []
	new_userpass = []
	pass_list = convert_list
		
	for element in range(random.randint(2, 4)):
		first_pos.append(random.choice(Alphabet_digits))
		
	for element in range(random.randint(2, 4)):
		last_pos.append(random.choice(Alphabet_digits))
	letter = ""

	for i in pass_list:
		letter += i
		random_letter = ''.join(choice((str.upper, str.lower))(char) for char in i)
		new_userpass.append(str(random_letter))

	first_pos.extend(new_userpass)
	first_pos.extend(last_pos)

	pre_effect(len(first_pos))
	result = ""
	for element in first_pos:
		result += element
			
		
	sys.stdout.flush()

	sys.stdout.write("\r")
	sys.stdout.write("Password: " + result + "                                ")
	print("\nMã hóa: " ,mahoa(result))

def generator_loop():
	generation()
	in_put = input("Thoát Chương Trình(Y/N): ")
	in_put.lower()
	while in_put != "y":
		generation()
		in_put = input("Thoát Chương Trình(Y/N): ")
		in_put.lower()

def edit_loop():

	edit()
	in_put = input("Thoát Chương Trình(Y/N): ")
	in_put.lower()
	while in_put != "y":
		edit()
		in_put = input("Thoát Chương Trình(Y/N): ")
		in_put.lower()
		if in_put == "y":
			introducion()

def introducion():
	print("Choose a Option\n1.Password Generator\n2.Edited Password")
	option = input("Option: ")
	if option == "1":
		generator_loop()
	elif option == "2":
		edit_loop()
introducion()