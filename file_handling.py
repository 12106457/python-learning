# File Handling
# File handling is used to store data permanently in Files.
# open() is used to open a file.
# "w" mode is used to write data.
# "r" mode is used to read data.
# "a" mode is used to add data to the file.
# "r+" mode is used to read and write data.
# close() is used to close the file


# file=open('dump.txt',"a+")
# name=input("Enter your name : ")
# age=int(input("Enter your age : "))
# address=input("Enter your address : ")
# phone=int(input("Enter your phone number : "))
# file.write(f"User Details:\nName : {name}\nAge : {age}\nAddress : {address}\nPhone : {phone}\n----------------\n")
# print("Thank you for your details")
# file.close()

file=open('dump.txt',"r")
# print(file.read())
file.seek(0)
for line in file.readline():
    print(line,end="")
    # print("-------------------")
