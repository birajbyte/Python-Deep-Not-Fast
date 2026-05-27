#DAy 17
# 1.Find the longest consecutive sequence in a list
nums = [5, 2, 99, 3, 4, 1, 6, 50, 51, 52]
nums = sorted(nums)
temp = []
result = []
current_sequence = 1
longest_sequence = 1
for i in range(len(nums)):
    if i < len(nums) - 1 and nums[i] + 1 == nums[i+1]:# for clean code is consecutive can be used
        current_sequence += 1# as it is same as the line i have written myself remember.
        temp.append(nums[i])
    else:
        temp.append(nums[i])
        longest_sequence = max(longest_sequence,current_sequence)
        current_sequence = 1
        if len(result) < len(temp):# for clean code result = max(result,temp,key = len)
            result = temp# above is same as the if statement 
        temp = []
print(f"{result} and count {longest_sequence}")
# 2. list Count how many elements appear exactly once
nums = [4, 3, 2, 7, 8, 2, 3, 1, 4, 4]
dic = {}
for num in nums:
    dic[num] = dic.get(num,0) + 1# first appear key update and next time value update 
count = 0
for key,value in dic.items():
    if value == 1:
        count += 1
print(count)
# 3. string Count occurrences of each vowel in a string
sentence = input("Enter  the string ").lower()
dic = {}
for letter in sentence:
    if letter in "aeiou":
        dic[letter] = dic.get(letter,0) + 1
print(dic)


 
