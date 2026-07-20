users= ["israel", "Jboy", "Moses"]
data =["Hope", 42, True]
emptylist = []

# print("israel" in users)
# print(users[0])
# print(users[-1])
# print(users.index("Moses"))
# print(users[1:3])
# print(users[-3:-1])
# print(users[1:])
# print(len(users))
# users.append("Hope")
# print(users)
# users += data
# users+= ["Favour"]
# print(users)
# users.extend(["Robert", "Jimmy"])
# print(users)
# users.extend(data)
# print(users)
# users.insert(0, "Babe")
# print(users)
# users[2:2] = ["Alex", "Eddy"]
# print(users)
# users[0:2] = ["benson", "Jp"]
# print(users)
# users.remove("israel")
# print(users)
# print(users.pop()) returns removedvalue
# print(users)
# del users[0]
# print(users)
# del data
# print(data)
# data.clear()
# print(data)

# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)

nums = [5, 55, 20, 1, 200, 100]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

# how to copy a list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "ben",True])
print(mylist)

# Tuples

mytuple = tuple(('dave', 23, True))
anothertuple = (1,2,2,3,4)
print(mytuple)
print(anothertuple)
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Niel")
newtuple = tuple(newlist)

print(newtuple)

(*one, two, all) = anothertuple
print(one)
print(two)
print(all)

print(anothertuple.count(2))



