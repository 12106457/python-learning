# we have 2 type of loop 
    #1. for loop # it will excecuted untill given range
    #2. while loop # it will excecuted only when codition is true

# looping in given range
for num in range(0,11):
    print(num,end=",")
print()

# looping in str
full_name = "sai kumar"

for char in full_name:
    print(char, end=" ")
print()

# print even number between 11-20 

for num in range(11,21):
    if num%2 == 0:
        print(num, end=",")
print()

skills = {"python","react","node"}

for index,skill in enumerate(skills):
    print(index , skill)

# while loop -> this will excecute only when condition true

name=""

while name=="":
    name=input("enter your name:")

print("enter name is:",name)



