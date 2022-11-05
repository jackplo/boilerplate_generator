import os  
import shutil

class CreateFile():

	def __init__(self, type):
		self.type = type

	def create(self, type=None):
		type = self.type
		directory = input("Enter desired project directory (include last /): ")
		while (os.path.isdir(directory) != True):
			directory = input("Invalid directory, enter a valid directory: ")

		if (directory[-1] != "/"):
			directory = directory + "/" + "main" + type
		else:
			directory = directory + "main" + type

		shutil.copyfile("./boilerplate/boilerplate" + type, directory)
		print("Completed... File can be located at: " + directory)


'''
To change:
make boilerplate code separate txt files
take a type input instead of number choice
read type specific file and copy the content to a new file in project directory (could use shutil or readlines)
handle directories better
add c++ and java
one function for all types instead of multiple functions for each type (a single create() function)
'''