# 1. dict Group anagrams together from a list of words
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dic = {}
for word in words:
    key = "".join(sorted(word))
    if key in dic:
        dic[key] += [word]
    else:
        dic[key] = [word]
print(dic)
# Easy way 
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dic = {}
for word in words:
    key = "".join(sorted(word))
    dic[key] = dic.get(key, []) + [word]
print(dic)

# 2.Generate all primes up to n using Sieve of Eratosthenes 
import math
n = int(input("Enter the n number to find the prime "))
prime = [True] * (n+1)
prime[0] = False
prime[1] = False
for i in range(2,math.isqrt(n)+1):
    for j in range(i*i,n+1,i):
        prime[j] = False
result = []
for num in range(2,n+1):
    if prime[num]:#same as if prime[num] == True
        result.append(num)
print(result)





