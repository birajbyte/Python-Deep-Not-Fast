#1. Find the smallest window in a list that contains all unique elements
lis = [2, 3, 1, 2, 3]
seen = set(lis)
dic = {}
left = 0
min_len = float('inf')
min_window = []
for right in range(len(lis)):
    dic[lis[right]] = dic.get(lis[right],0) +1
    while all(dic.get(x,0) >=1 for x in seen):
        if min_len > right - left +1:
            min_len = right - left + 1
            min_window = lis[left:right+1]
        dic[lis[left]] -= 1
        left += 1
print(min_window)
#2. list Find all triplets in a list that sum to zero
lis = [-1, 0, 1, 2, -1, -4]
for i in range(len(lis)):
    for j in range(i+1, len(lis)):
        for k in range(j+1, len(lis)):
            if lis[i] + lis[j] + lis[k] == 0:
                print(f"REquired triplets are {lis[i]},{lis[j]},{lis[k]}")

#3. string Find the longest common prefix among a list of strings
words = ["flower", "flow", "flight"]
lis = []
st = st = min(words, key=len)
for i in range(len(words)):
    if all(st[i] == word[i] for word in words):
        lis.append(st[i])      
print("".join(lis))
