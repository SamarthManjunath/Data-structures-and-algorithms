#learning the use of hash tables - dictionary

#creating a hash table all at once
items = dict({"key1": 1, "key2": 2, "key3": 3})

#print the hashtable
print(items)

#creating a hash table progressively
items1 = {} #empty hash table
items1["key1"] = 1
items1["key2"] = 2
items1["key3"] = 3
items1["key4"] = 4

#accessing a key which is not present
#print(items["key4"])

items1["key2"] = "two"
print(items1)

#iterating keys and values
for key, values in items1.items():
	print(key, values)

