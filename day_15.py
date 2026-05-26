# Day 15
# 1.Find LCM of two numbers
# least common multiple means when two number can be at same point
num1 = int(input("Enter the number "))
num2 = int(input("Enter the number "))
for i in range(1,num1 * num2):# 3 & 4 lcm is 12 so i check another find
    a= num1 * i
    if a % num2 == 0:
        print(f"LCM IS {a}")
        break
# 2.list Find the majority element (appears more than n/2 times)
lst = [2, 2, 1, 2, 1, 2]
n = len(lst) / 2
dic = {}
for num in lst:
    dic[num] = dic.get(num,0) + 1
for key , value in dic.items():
    if value > n:
        print(f"Element found apeared  {value} times is {key}")
        break
# Boyer-Moore Voting Algorithm
candidate = None
count = 0
for new in lst:
    if count == 0:
        candidate = new
        count += 1
    if new == candidate:
        count += 1
    else:
        count -= 1
# verify candidate is actual majority
print(f"Majority element is {candidate}")
if lst.count(candidate) > len(lst) // 2:#list.count(el) is method in LIst
    print(f"Majority element is {candidate}")
else:
    print("No majority element exists")
# 3.list Separate odd and even numbers keeping order
original = [3, 1, 4, 1, 5, 9, 2, 6]
even = []
odd = []
for num in original:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
result = even + odd
print(result)
#Partition method or pointer method without pivot element
lst = [3, 1, 4, 1, 5, 9, 2, 6]#here order is not maintained but new concept
left = 0                    # starts from beginning
right = len(lst) - 1        # starts from end

while left < right:
    if lst[left] % 2 ==0:
        left += 1
    elif lst[right] %2 != 0:
        right -= 1
    else:
          lst[left],lst[right] = lst[right],lst[left]
          right -= 1
          left += 1
print(lst)



