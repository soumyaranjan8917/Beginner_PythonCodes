''' Label the program written in problem 4 with comments '''

import os

# Specify the directory path (use '/' for the current directory)
# directory_path = '/'
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# print each file and directory name
print("Directory Contents:")
for item in contents:
    print(item)

