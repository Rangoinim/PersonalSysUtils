# A test program to help understand how directory listing works
# Also a test in file output

# Imports for program

import os

# Global variables
LOCAL_PATH = os.getcwd()

# Beginning of function
# Saves a path to a text file
def savePathToFile(directory):
    if os.path.exists(directory):
        with open('dirOutput.txt', 'w') as file:
            file.write(directory)
    else:
        print("Not a valid directory, please try again")
    
    return directory

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

# Beginning of searchDirectory
# Searches for files based on a string and opens it if requested
def searchDirectory(directory):
#   Local variables

    numMatches = 0
    matchesRemaining = 0
    searchTerm = input("Please enter either the name of the file or a subset of the name: ")
    confirm = ""
    
#   Function
    with open('dirList.txt', 'r') as file:
        while file.readline() != '':
            line = file.readline()
            if searchTerm in line:
                numMatches += 1
    print(f'There are {numMatches} files that match the search term provided. Listing them now...')
    with open('dirList.txt', 'r') as file:
        while file.readline() != '' and confirm != "stop":
            line = file.readline()
            line = line.rstrip('\n')
            matchesRemaining = numMatches
            if searchTerm in line:
                matchesRemaining -= 1
                confirm = input(f'File {line} found!\nWould you like to open it? (y/n/stop)')
                if confirm == 'y':
                    os.chdir(directory)
                    os.startfile(line)
                    print(f'File opened! There are {matchesRemaining} files remaining.')
                elif confirm == 'n':
                    print(f'There are {matchesRemaining} files remaining. Moving to the next file...')
                elif confirm == 'stop':
                    print("Exiting...")
                    os.chdir(LOCAL_PATH)

# Beginning of mainMenu

def mainMenu():
	print("MAIN MENU\n",
	"================================\n",
	"1: List selected directory\n",
	"2: Save a directory to a text file\n",
	"3: Save directory listing to a file\n",
    "4: Search directory listing for a file\n",
	"Anything else to quit")
	choice = input("Choose an option: ")
	if choice.isdigit() and int(choice) >= 1 and int(choice) <= 4:
		return int(choice)
	else:
		return 0

# Beginning of main
        
def main():
    directory = input("Please enter the path of the directory you want scanned: ")
    choice = mainMenu()
    if choice == 0:
        print("later gamers")
    elif choice == 1:
        print(LOCAL_PATH)
    elif choice == 2:
        workingDirectory = savePathToFile(directory)
    elif choice == 3:
        workingDirectory = saveDirToFile(directory)
    elif choice == 4:
        searchDirectory(directory)
    
main()
# End of main