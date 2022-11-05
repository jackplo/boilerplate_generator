from GUI import GUI
from CreateFile import CreateFile

def main():
	gui = GUI()
	choice = gui.main_menu()
	type = None

	if choice == "1":
		type = ".py"
		CreateFile(type).create()

	if choice == "2":
		type = ".cpp"
		CreateFile(type).create()

	if choice == "3":
		type = ".java"
		CreateFile(type).create()

	if choice == "4":
		print("WIP...")
		return 

if __name__ == "__main__":
	main()