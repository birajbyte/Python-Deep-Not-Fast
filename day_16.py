#day 16 
# 1.Find the first non-repeating character in a string
word = input("Enter the string ")
dic = {}
for letter in word:
    dic[letter] = dic.get(letter,0) + 1
for key,value in dic.items():
    if value == 1:
        print(f"{key}:{value}")
        break# only one which appear for the first time no only non repeating that's diff

# 2. Build a frequency table from a list of tuples
data = [
    ("apple", 3),
    ("banana", 2),
    ("apple", 5),
    ("mango", 1),
    ("banana", 4),
    ("mango", 3),
    ("apple", 2),
    ("cherry", 7),
    ("banana", 1),
    ("cherry", 3)
]
dic = {}
for key,value in data:
    dic[key] = dic.get(key,0) + value
for key,value in dic.items():
    print(f"{key}:{value}")

# 3. Sum of digits of a number until it becomes single digit
num = int(input("Enter the number "))#used string or type casting in solution
while num >= 10:
    total = 0
    for d in str(num):
        total += int(d)
    num = total
print(num)
#Math version is more prefered
while num >=10:# for this single digit problem this is the edge case num range = 0-9
    total = 0
    temp = num
    while temp > 0:
        total += temp % 10 # reducing extra variable reminder clean code
        temp = temp // 10
    num = total
print(num)



