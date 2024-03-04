from os import system, path, get_terminal_size
window_width = get_terminal_size().columns

from datetime import date
today = date.today().strftime("%B %d, %Y")
#########################################################################################
def header():
	system("cls||clear")
	print("\n\n"+"{0} {1}".format("Edin Mehanovic CIS125 Structure and Logic", today).center(window_width)+"\n\n")
#########################################################################################
def center(phrase):
	phrase = str(phrase)
	return ('%s'.center(get_terminal_size().columns-len(phrase))%phrase)
#########################################################################################
def input_center (phrase):
	return input("".ljust((window_width - len(phrase))//2)+ phrase)	
#########################################################################################
def read_file(my_file):
	global dictionary_words
	dictionary_words = {}
	file = open(my_file, "r", encoding='utf-8')
	for line in file:
		line = line.strip()
		translated_word = line.split("\t")
		dictionary_words[translated_word[0]] = translated_word[1]	
#########################################################################################
def file_check(my_file):
	if path.isfile(my_file):
		read_file(my_file)
	else:
		print((my_file +" does not exist!!!").center(window_width))
#########################################################################################
def translator_input():
	global translate_input
	translate_input = input_center("Enter an English word or phrase you wish to translate: ").lower().strip()
#########################################################################################
def translator_process():
	global russian_list, english_list, length_list
	length_list = []
	russian_list = []
	english_list = translate_input.split(" ")
	for i in english_list:
		if i in dictionary_words:
			russian_list += [dictionary_words[i]]
		else:
			russian_list += ["???"]
		if len(russian_list[-1]) > len(i):
			length_list += [len(russian_list[-1])]
		else:
			length_list += [len(i)]
#########################################################################################	
def translator_output():
	center_string1 = " | "
	center_string2 = " | "
	for i in range(len(english_list)):
		center_string1 += (russian_list[i].ljust(length_list[i])+" | ")
		center_string2 += (english_list[i].ljust(length_list[i])+" | ")
	print("\n\n")
	print(center(center_string1),"\n")
	print(center(center_string2))
	print("\n\n")
#########################################################################################
def main_bus(repeat = 'y'):
	if repeat == 'n' or repeat == 'N':
		print("\n\n\n")
		print(center('''"Have a nice day!"\n'''))
		input_center("Press <Enter> to continue... ")
		return
	elif repeat == 'y' or repeat == 'Y':
		read_file("EngRus.txt")	
		header()
		translator_input()
		translator_process()
		translator_output()
		repeat = input_center("Would you like to run the program again (Y/N): ")
		main_bus(repeat)
	else:
		print("\n\n")
		print(center(repeat+" is an invalid entry\n\n"))
		repeat = input_center("Would you like to run the program again (Y/N): ")
		main_bus(repeat)
		
main_bus()
