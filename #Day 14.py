#Day 14
# Find all permutations of a short string (no library)
#Pure logic thinked by me works for only up to len 3
word = input("Enter the string ")
if len(word) > 1:
    permu = []
    a = word
    rev = word[::-1]
    b = rev
    for _ in range(len(word)):
        permu.append(word)
        word = word[-1] + word[:len(word)-1]
        if a == word:
            break
    for _ in range(len(rev)):
        permu.append(rev)
        rev = rev[-1] + rev[:len(rev)-1]
        if b == rev:
            break
    permu = list(dict.fromkeys(permu))
    print(permu)
else:
    print(word)
# # REcursion version that works for most of the len words
word = input("Enter the string: ")
results = []
def permute(current, remaining):
    if remaining == "":
        results.append(current)
        return
    for i in range(len(remaining)):
        permute(current + remaining[i], remaining[:i] + remaining[i+1:])
permute("", word)

for p in results:
    print(f"{p}")

# 2.Find the missing number in a list of 1 to n
arr = [6, 3, 1, 5, 8, 7, 2]
arr = sorted(arr)
for i in range(len(arr)):
    if arr[i] == i+1:
        continue
    else:
        print(f"Required missing number is {i+1}")
        break 
# solution without sorted and sum formul
arr = [6, 3, 1, 5, 8, 7, 2]
s = set(arr) # used as no unordered so 
for i in range(1,len(arr)+2):
    if  i not in s: #here it check super fast than list as it is orderd check one by one
        print(f"Required missing number is {i}")
# 3. Split a list into two halves
arr = [1,2,3,4,5]
arr_1= []
arr_2 = []
n = len(arr) // 2
print(n)
for i in range(n):
    arr_1.append(arr[i])
for i in range(n,len(arr)):
    arr_2.append(arr[i])
# print(f"Requred half list 1 {arr_1} and list 2 {arr_2}")
# #pythonic way 
arr = [1,2,3,4,5,6]
n = len(arr) // 2
arr_1 = arr[:n]
arr_2 = arr[n:]
print(f"List 1 {arr_1} and List 2 {arr_2}")