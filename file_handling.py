# File Handling
# File handling is used to store data permanently in Files.
# open() is used to open a file.
# "w" mode is used to write data.
# "r" mode is used to read data.
# "a" mode is used to add data to the file.
# "r+" mode is used to read and write data.
# close() is used to close the file


file=open('dump.txt',"w")
file.write("Hello World")
file.close()