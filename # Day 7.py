# Day 7
# Find the longest word in a sentence
sentence = input("Enter the sentence")
words = sentence.split()
a = ""
for word in words:
    if len(a ) < len(word):
        a = word
print(f"REquired longest word is  {a}")

#  Merge two sorted lists without sort()
a = [5, 1, 8]
b = [3, 9, 2]
c = []
for num in a:
    c.append(num)
for num in b:
    c.append(num)

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i] > c[j]:
            temp = c[i]
            c[i] = c[j]
            c[j] = temp
print(c)

# Group words by their first letter
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
dic = {}
for word in words: #in just check whether exist or not
    if word[:1] in dic:
        dic[word[:1]].append(word)
    else:
        dic[word[:1]] = [word]
       
print(dic)
    