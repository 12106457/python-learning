# List comprehension:- It is a short way to create a new list from an existing iterable
# basic Syntax: [expression for item in iterable]

# example
# normal way
numbers = [1, 2, 3, 4, 5]

squares = []

for num in numbers:
    squares.append(num * num)

print(squares)

# using list comprehension

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)

# example 2

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers if num % 2 == 0]

print(squares)