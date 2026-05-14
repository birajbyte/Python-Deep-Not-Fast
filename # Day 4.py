# Day 4
# 1. math Find all prime factors of a number
number = int(input("Enter the nubber to get prime factor  "))
result = []
if number > 1:
    for num in range(2,number):
        if number % num == 0:
            print("The number is not prime now we have to get prime factor\n")
            break
    else:
        print("Required prime factor of number is ",number)
    i = 2
    while number > 1:
        if number % i == 0:
            result.append(i)
            number = number // i #when working with whole numbers always use //
        else:
            i += 1

    print("The required prime factors is ",*result)
else:
    print("Enter the number greater than one")
# 2. string Check if a string is a pangram
#Pangram is type of string that contains all 26 alphabets
import string 
sentence = input("Enter the string to check ")
words = sentence.split()
word = "".join(words).lower()
word = sorted(set(word))
word = "".join(word)
word2 = string.ascii_lowercase

if word == word2:
    print("The given string is pangram")
# #more advance version 
import string
sentence = input("Enter string: ")
alphabet = set(string.ascii_lowercase)
sentence_letters = set(sentence.lower())
if alphabet.issubset(sentence_letters):#issubset means element of alph contain
    print("Pangram!")#in sentence_letters math subset concept 
else:
    print("Not a Pangram!")

# 3.  Rotate a list by n positions (left and right)
n = int(input("Enter the number"))
a = [1,2,3,4,5]
result_left = a[n:] + a[:n]#rotation of number from leftToRight n fall from 1st
result_right= a[-n:] + a[:len(a)-n]#rotation of n from leftToRight nFallfromLAST 
print(f"Required left rotate is {result_left}")
print(f"Required right rotate is {result_right}")

# 4.  Find all pairs in a list that sum to a target
# task is to find two numbers (all pairs) from the list whose sum = target.
nums = [1,2,3,4,5,6,7]
target = int(input("Enter the number "))
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        total = nums[i] + nums[j]
        if total == target:
            print(f"({nums[i]},{nums[j]})")          
# 5. dict Merge two dicts and sum values of common keys
result = {}
d1 = {"apple": 10,"banana": 5,"mango": 8}
d2 = {"banana": 7,  "orange": 12,"mango": 2}
for key in d1:
    if key in d2:
        result[key] = d1[key] + d2[key]
    else:
        result[key] = d1[key]

for key in d2:
    if key not in d1:
        result[key] = d2[key]

print(f"Required merged dictionary {result}")

