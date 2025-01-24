'''
Write an python program to print the contains of a directory using the OS module. 
Search online(CHAT GPT) for the function which does that
'''
import os

# Specify the directory path (use '.' for the current directory)
# directory_path = '/'
directory_path = '/Wallpaper'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
print("Directory Contents:")
for item in contents:
    print(item)
