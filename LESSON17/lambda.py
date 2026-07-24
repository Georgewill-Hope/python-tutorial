from functools import reduce

squared = lambda num : num * num
print(squared(3))

addTwo = lambda num : num + 2
print(addTwo(8))

sum_total = lambda a, b : a + b
print(sum_total(2, 5))

######################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))


#######################################

numbers = [2, 3, 7, 12, 18, 20, 45, 37]

squarednums = map(lambda num : num * num, numbers)
print(list(squarednums))

odd_nums = filter(lambda num : num % 2 != 0, numbers)
print(list(odd_nums))

#########################################



numbers = [1,2,3,4,5,6,1]

total = reduce(lambda acc, curr : acc + curr, numbers,10)

print(sum(numbers,10))
print(total)


names = ["Hope", "John Wilson", "Dominic schloterbieck"]

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(char_count)