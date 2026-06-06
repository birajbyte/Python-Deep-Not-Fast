# 1. dict Group anagrams together from a list of words
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# dic = {}
# for word in words:
#     key = "".join(sorted(word))
#     if key in dic:
#         dic[key] += [word]
#     else:
#         dic[key] = [word]
# print(dic)
#Easy way 
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dic = {}
for word in words:
    key = "".join(sorted(word))
    dic[key] = dic.get(key, []) + [word]
print(dic)

# 2.Generate all primes up to n using Sieve of Eratosthenes 
n = int(input("Enter the n number to find the prime"))
result = []
for num in range(2,n+1):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        result.append(num)

print(result)