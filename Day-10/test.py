# Reading input from the user
#folders = input("Please provide list of folders name with spaces in between:" ).split()

#print(folders)

# Writing for loop to list out the file in a sequence manner

#folders = input("Please provide list of folders name with spaces in between:" ).split()

#for folder in folders:
#    print(folder)

# Identify the module
import os

folders = input("Please provide list of folders name with spaces in between:" ).split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like this folder does not exists:" + folder)
        continue # To ignore the wrong folder name and proceed with next use continue instaed of break
    except PermissionError:
        continue
        print("No access to this folder" + folder)

    print(" ==== listing files for the folder -" + folder)

    for file in files:
        print(file)