from GUI import GUI
from CreateFile import CreateFile

def main():
	gui = GUI()
	choice = gui.main_menu()
	type = None
	print(choice)

	if choice == "1":
		type = "python"
		CreateFile("python").createPython()



if __name__ == "__main__":
	main()