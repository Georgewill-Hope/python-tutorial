# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(type(band))
print(band2)
print(len(band2))

# Access items

print(band["guitar"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band2.items())

# verify a key exists
print("vocals" in band)
print("drum" in band)

# change values
band["vocals"] = "Cymbals"
band.update({"bass":"JPJ"})

print(band)

# remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Hope"
print(band)
print(band.popitem()) # tuple
print(band)

# Delete and clear
band["drums"] = "Hope"

del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries

# band2 = band # creates a refference
# print("Bad Copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

band3 = dict(band)
print("Good copy!")
print(band3)

# Nested dictionaries

member1 = {
    "name" : "Plant",
    "instrument": "Vocals"
}
member2 = {
    "name" : "Page",
    "instrument": "Guitar"
}

band = {
    "member1": member1,
    "member2": member2,
}

print(band)
print(band["member1"]["name"])

# Sets

nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# Sets does not allow duplicates
nums = {1,2,2,3}
print(nums)

# True value is a dupe of 1 and False is a dupe of 0
nums = {1,True, 2, False,3,4,0}
print(nums)

# check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from on set to another

morenums = {5,6,7}
nums.update(morenums)
print(nums)

# you can use update with list, tuples and dict, too

# merge two sets to create a new set
one= {1,2,3}
two={5,6,7}

mynewset=one.union(two)
print(mynewset)

# Keep only the duplicate
one= {1,2,3}
two={2,3,7}

one.intersection_update(two)
print(one)

# Remove duplicates
one= {1,2,3}
two={2,3,7}

one.symmetric_difference_update(two)
print(one)