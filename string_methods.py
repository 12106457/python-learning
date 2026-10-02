#string method are inbuild method we can use those method for formatting text

name="sai kumar"
city = "    rjy    "
print(name.upper()) #convert into upper case
print(name.lower()) # convert into lower case
print(name.capitalize()) # convert into capitalize
print(name.title()) # convert into camel case
print(name.replace("kumar","suresh")) # replace the text
print(city.strip()) # remove the front and back spaces
print(name.split(" ")) # it split sentence into word and give in list
print(name.isdigit()) # return bool by checking text is digit 
print(city.strip().isalpha()) # return bool by checking text is character
print(name.startswith("s")) # return bool by checking character start with that character
print(name.endswith("rl"))# return bool by checking character end with that character

print("123".isdigit())       # True
print("Hello".isalpha())     # True
print("Hello123".isalnum())  # True
print("hello".islower())     # True
print("HELLO".isupper())     # True

print(''.join(['a', 'b', 'c'])) # 'abc'


# fstring (formatted string literal)
# it is smiliar to template literal in js
# using this we can insert variable , experssoon directly into string.
name="sai"
age=24
city="rjy"

print(f"my name is {name} and my age is {age}. i belong to {city}")