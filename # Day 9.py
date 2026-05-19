# Day 9
# math Find GCD of two numbers without math module
#GCD mean Greatest common divisor that divides both evenly
# num1 = 12
# num2 = 8
# l = []
# for num in range(1,num2+1):
#     if num1 % num ==0 and num2 % num == 0:
#         l.append(num)
# gcd = float("-inf")
# for i in l:
#     if gcd < i:
#         gcd = i
# print(f"REquired greates common diviser is {gcd}")
#Euclidean method to solve more efficiently
a,b = 12,8#through recursion also it is possilbe to do
while b != 0:
    a,b = b,a % b
print(a)


# 2. string Count how many words start with a vowel
sentence = input("Enter the sentence ")
words = sentence.lower().split()
count = 0
for word in words:
    if word[:1] in "aeiou":
        count += 1
print(f"Required count of words are {count}")

# 3. string Check if a sentence is a palindrome (ignore spaces)
sentence = input("Enter the sentence")
words = sentence.lower().split()
word = "".join(words)
rev_word = word[::-1]
if word == rev_word:
    print("Given sentence is pallindrome")
else:
    print("NOt pallindrome")