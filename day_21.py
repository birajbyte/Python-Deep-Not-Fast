# 1  Find the longest substring with no repeating characters
word = input("Enter the string ")
seen = set()
compare = ""
longest = ""
for char in word:
    if char not in seen:
        seen.add(char)
        compare += char
    else:
        if len(longest) < len(compare):
            longest = compare
        seen = set()
        compare = ""
if len(longest) < len(compare):
    longest = compare
print(longest)
# #more efficient way SLIDING WINDOW WITH SET
word = input("Enter string: ")
seen = set()
left = 0
longest = 0
start = 0

for right in range(len(word)):
    while word[right] in seen:
        seen.remove(word[left])
        left += 1
    seen.add(word[right])
    if right - left + 1 > longest:
        longest = right - left + 1
        start = left

print(word[start : start + longest])
# 2 dict Nested dict: store students with name and marks, print topper
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]
marks = float("-inf")
for key, value in students: 
    if marks < value:
        marks = value
        name = key
print(f"Topper {name}:{marks}")
#nested dictionary type value[marks] direct excess to value of key
students = {
    "Alice": {"marks": 85},
    "Bob": {"marks": 92},
    "Charlie": {"marks": 78}
}

marks = float("-inf")
name = ""

for key, value in students.items():
    if marks < value["marks"]:
        marks = value["marks"]
        name = key

print(f"Topper {name}: {marks}")

# 3 math Check if a number is a happy number 
num = int(input("Enter the number"))
seen = set()
seen.add(num)
while num != 1 :
    total = 0
    while num > 0:
        rem = num % 10
        total += rem**2
        num = num // 10
    num = total
    if num in seen:
        print("NOt happy number")
        break
    seen.add(num)
else:
    print("Happy number")






