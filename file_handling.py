# File Handling
# File handling is used to store data permanently in Files.
# open() is used to open a file.
# "w" mode is used to write data.
# "r" mode is used to read data.
# "a" mode is used to add data to the file.
# "r+" mode is used to read and write data.
# close() is used to close the file

# available methods:
# open() // to open/create file 
# close() // to close the open file 
# write() //to write/append the content 
# read() // it read entire file and return the data inside the file
# readline() // it read the one line 
# readlines() //it read entire line return data in list format
# seek(index) // it used to set the cursur point 
# with open() // it automatically open and close the file when it done with file.

# file=open('dump.txt',"a+")
# name=input("Enter your name : ")
# age=int(input("Enter your age : "))
# address=input("Enter your address : ")
# phone=int(input("Enter your phone number : "))
# file.write(f"User Details:\nName : {name}\nAge : {age}\nAddress : {address}\nPhone : {phone}\n----------------\n")
# print("Thank you for your details")
# file.close()
# -----------------

# without with 
# file=open('dump.txt',"r")
# # print(file.read())
# file.seek(0)
# for line in file.readline():
#     print(line,end="")
#     # print("-------------------")

# -----------------
# with open
with open('dumps.txt','r') as file:
    data=file.read()
    print(data)



