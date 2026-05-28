 # Day 18
# Merge a list of dicts into one dict
# lis = [{"a": 1}, {"b": 2}, {"a": 5}]
# dic = {}
# for dis in lis:
#     for key in dis:
#         dic[key] = dis[key]
# print(dic)
# Find the second most frequent element in a list/2,2,2 and 3,3,3,3 ans 2
# l = [5, 2, 5, 3, 2, 8, 5, 3, 2, 3, 3, 7, 8, 8]
# dit = {}
# for num in l:
#     dit[num] = dit.get(num,0) + 1
# print(dit)
# largest = float("-inf")
# second  = float("-inf")
# for value in dit.values():
#     if largest < value:
#         second = largest
#         largest = value
#     elif second < value and value != largest:
#         second = value
# for key,value in dit.items():
#     if value == second:
        # print(f"{key}:{value}")
# Chunk a list into groups of size n
n = int(input("Enter the number"))
l = [1, 2, 3, 4, 5, 6, 7]
#when i need to control the index than while loop
i = 0
while i < len(l):
    print(l[i:i+n])
    i = i + n