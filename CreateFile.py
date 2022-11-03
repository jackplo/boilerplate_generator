class CreateFile():

	def __init__(self, type):
		self.type = type

	def createPython(self):			
		try:
			directory = input("Enter desired Directory (Include last backslash): ")
			directory = directory + "main.py"

			with open(directory, "w") as file_obj:
				file_obj.write("\n\n__author__ = \"Your Name\"\n__version__ = \"0.1.0\"\n__license__ = \"MIT\"\n\ndef main():\n    print(\"Hello World\")\n\n\nif __name__ == \"__main__\":\n    main()")

		except FileNotFoundError:
			print("Error creating file. Please try again.")
		else:
			print("New project can be located at " + directory)



'''
To change:
make boilerplate code separate txt files
take a type input instead of number choice
read type specific file and copy the content to a new file in project directory (could use shutil or readlines)
handle directories better
add c++ and java
one function for all types instead of multiple functions for each type (a single create() function)
'''