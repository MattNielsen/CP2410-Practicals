#1. Multiple Finder - n = multiple of m.
def is_multiple(n, m):
    if n == 0:
        return False
    elif n % m == 0:
        return True
    else:
        return False

#Test cases
print(is_multiple(10,5))
print(is_multiple(1,5))
print(is_multiple(0,5))
print(is_multiple(155,5))

# 2. List Comprehension.
y = [1,2,3,4,5]

listComprehensionOne = [x * 2 for x in y]
listComprehensionTwo = [x * x for x in range(13)]
print("Example 1 - ", listComprehensionOne,"\nExample 2 -", listComprehensionTwo)
# 3. Duplicate number finder.
def findUniqueNumber(number=0):
    sequenceCountStr = str(number)
    for numbers in sequenceCountStr:
        counter = 0
        for numbers2 in sequenceCountStr:
            if numbers == numbers2:
                counter += 1
        if counter >= 2:
            print("Not all numbers are unique. Duplicate number found for number = ", numbers)
# Test cases

# No duplicates found.
findUniqueNumber(123456)
# Duplicate found for 1 and 2.
findUniqueNumber(12234561)
# Duplicate found for 8 and 9.
findUniqueNumber(98012348967)

# 4. generators.

# The list version.
def harmonic_list(n):
    result = []
    h = 0
    for i in range(1, n+1):
        h += 1 / i
        result.append(h)
    return result

print(harmonic_list(6))

# Generator using Yield.
def harmonic_generator(n):
    h = 0
    for i in range(1, n+1):
        h += 1 / i
        yield h
# Output
for i in harmonic_generator(6):
    print(i)

