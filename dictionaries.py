print("dictionary")

dic = {
    "name":"sai",
    "age":26,
    "city":"rjy"
}
copy_dic=dic.copy() # create a shallow copy

dic["name"]="kumar" # update the pair
dic.update({"age":24,"city":"KKD"}) # update the pairs
print(dic.keys()) # return all keys
print(dic.values()) # return all values
print(dic.items()) # return like key + value

keys=dic.keys()
for key in keys:
    print(key," : ",dic[key])
dic.pop("name") #remove specified key
dic.popitem() # remove last key value pair
del dic["age"] # remove specified key value pait
dic.clear() # it clear all key value pair

print(dic)
print(copy_dic)
