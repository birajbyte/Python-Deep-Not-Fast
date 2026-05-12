#Day 2
# 1. math Check Armstrong number
num=int(input("Enter the number to check Armsrong  "))
arm=0
pow=len(str(num))
a=num
while num>=1:
    rem= num % 10
    arm= arm + rem**pow
    num=num //10
if a == arm:
    print("The given number is armstrong")
else:
    print("The number is not armstrong")

# 2. math Compute nth Fibonacci iteratively
#Every number is the sum of previous2number  and start from zero called fibo S

num = int(input("Enter the number upto where series to be printed "))
first_num = 0
second_num = 1
if num > 1:
    print(first_num,second_num,end=" ")
    for _ in range(num-2):
        a = first_num + second_num
        first_num = second_num
        second_num = a
        print(a,end=" ")
else:
    print( first_num)
# 3. string Check if two strings are anagrams
#Anagrams are those contain same letters but different order listen and silent
word1 = input("Enter the first string ")
word2 = input("Enter the second string ")
dict_1 = {}
for word in word1:
    if word in dict_1:
        dict_1[word] += 1
    else:
        dict_1[word] = 1
dict_2 = {}
for word in word2:
    if word in dict_2:
        dict_2[word] += 1
    else:
        dict_2[word] = 1

if dict_1 == dict_2:
    print("Given string are Anagram")
else:
    print("Given string arenot Anagram")
# 4. list Find second largest number without sort()
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
largest = float("-inf")
second_largest = float("-inf")
for num in numbers:
    if largest < num:
        second_largest = largest
        largest= num
    elif num != largest and num > second_largest:
        second_largest = num
print("REquired second largest is  ",second_largest)

# 5. dict Group numbers as even/odd using a dict
numbers = [64, 34, 25, 12, 22, 11, 90, 45, 7, 78]
even = []
odd = []
result = {}
for i in numbers:
    if i % 2 == 0:
        even.append(i)  
    else:
        odd.append(i)
result["even"] = even
result["odd"] = odd
print(result)
