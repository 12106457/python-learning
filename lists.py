
#list-> it is collection of items which is ordered and mutable.

array=[1,1,2,4,5]
str=["sai","kumar","suresh"]

print(len(array))
print(array.count(1))

findelement = 2
if findelement in array:
    print(array.index(2))
else:
    print(f"{findelement} is not given collection")

array.append(3) #add item at last
array.insert(0,10) # add item at specified index
array.extend([20,11]) # add multiple item into collection 
array.remove(11) # remove item by value
array.pop() # remove item without params remove at last with params remove specified index
del array[0] # remove item based on index
array.sort() # sort the list by default ascending order 
array.sort(key=abs,reverse=False) # sort the list in descending order
array.reverse() # reverse the list
str.sort(key=len,reverse=False)
print(array)
print(str)