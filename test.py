# A test program to help understand how directory listing works
# Also a test in file output

# Imports for program

import os
from PIL import Image

# Global variables
LOCAL_PATH = os.getcwd()

# Saves a path to a text file
def savePathToFile(directory):
    if os.path.exists(directory):
        with open('dirOutput.txt', 'w') as file:
            file.write(directory)
    else:
        print("Not a valid directory, please try again")

# Saves the directory listing of the path provided   
def saveDirToFile(workingDirectory):
    os.chdir(workingDirectory)
    dirList = os.listdir(path=workingDirectory)
    os.chdir(LOCAL_PATH)
    if os.path.exists(workingDirectory):
        try:
            with open('dirList.txt', 'w') as file:
                file.write('\n'.join(dirList))
        except OSError:
            print("Error!")
    else:
        print("Not a valid directory, please try again")

# Searches for files based on a string and opens it if requested
def searchDirectory(directory):
#   Local variables

    numMatches = 0
    searchTerm = input("Please enter either the name of the file or a subset of the name: ")
    confirm = ""
    
#   Function
    with os.scandir(directory) as curDirectory:
        for entry in curDirectory:
            if searchTerm in entry.name and entry.is_file():
                print(entry.name)
                
# Opens a file in a provided directory
def openFiles(directory):
    
    searchTerm = input("Please enter either the name of the file or a subset of the name: ")
    matchesRemaining = 0
    confirm = ""
    
    # Do an initial scan to check how many files match the searchTerm
    with os.scandir(directory) as curDirectory:
        for entry in curDirectory:
            if searchTerm in entry.name and entry.is_file():
                matchesRemaining += 1
    # Iterate through the directory and prompt opening for any files in the directory
    with os.scandir(directory) as curDirectory:
        for entry in curDirectory:
            if searchTerm in entry.name and entry.is_file() and matchesRemaining != 0:
                matchesRemaining -= 1
                confirm = input(f'File {entry.name} found!\nWould you like to open it? (y/n/stop)')
                if confirm == 'y':
                    os.chdir(directory)
                    os.startfile(entry.name)
                    print(f'File opened! There are {matchesRemaining} files remaining.')
                elif confirm == 'n':
                    print(f'There are {matchesRemaining} files remaining. Moving to the next file...')
                elif confirm == 'stop':
                    print("Exiting...")
                    curDirectory.close()
            elif matchesRemaining == 0 and confirm == "":
                print("No matches found. Returning to main menu...")
                   
# def batchRename(directory):
    

# Presents selection options for user
def mainMenu():
	print("MAIN MENU\n",
	"================================\n",
	"1: List selected directory\n",
	"2: Save a directory to a text file\n",
	"3: Save directory listing to a file\n",
    "4: Search directory listing for a file\n",
    "5: Open a specified file\n",
	"Anything else to quit")
	choice = input("Choose an option: ")
	if choice.isdigit() and int(choice) >= 1 and int(choice) <= 5:
		return int(choice)
	else:
		return 0

# Beginning of main
        
def main():
    directory = input("Please enter the path of the directory you want to work in: ")
    choice = mainMenu()
    if choice == 0:
        print("later gamers")
    elif choice == 1:
        print(LOCAL_PATH)
    elif choice == 2:
        savePathToFile(directory)
    elif choice == 3:
        saveDirToFile(directory)
    elif choice == 4:
        searchDirectory(directory)
    elif choice == 5:
        openFiles(directory)
    
main()
# End of main