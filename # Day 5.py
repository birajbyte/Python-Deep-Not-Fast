# Day 5
# 1. Compute factorial without recursion
number = int(input("Enter the number to find factorial "))
#using while loop
fact = 1
i = 1
while i <= number:
    fact = fact * i
    i += 1
print(f"Required Factorial using while loop is {fact}")
# for loop 
a = 1
for i in range(1,number+1):
    a = a * i
print(f"Required factorial using for loop is {a}")
# 2. Compress a string: aabbb -> a2b3
word = input("Enter the string ")
result = []
i = 0
while i < len(word):
    count = 1
    while i + count < len(word) and word[i] == word[i+count]:
        count += 1
   

    result.append(word[i] + str(count))
    i += count

print("".join(result))

# 3. Flatten a nested list manually
#flattend mean change nested list to one list eg-[1,[2,3]] to [1,2,3]
def flatten(lst):
    result = []
    for element in lst:
        if type(element) == list:
          result.extend(flatten(element))
        else:
            result.append(element)
    return result

given_list = [1, [2, 3], [4, [5, 6]], 7]
print(flatten(given_list))


