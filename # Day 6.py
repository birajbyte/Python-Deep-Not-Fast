# Day 6
# 1.Invert a dictionary (swap keys and values)
dic = {"a":1,"b":2,"c":3,"d":4}
a = {}
for key,values in dic.items():
    a[values] = key
print(a)
# 2. Count digit frequency of a number using a dict
dic = {}
users_input = input("Enter the digits")
for value in users_input:
    value = int(value) #changing key to integer small but useful concept
    if value in dic:
        dic[value] += 1
    else:
        dic[value] = 1
print(dic)
# Print all perfect numbers up to 1000
#The number whose factors sum is equal to number itself called perfect number
#factors of 6 = 1,2,3,6 but the number itself is ignored 1+2+3=6 so p_number
result = []
for num in range(1,1000):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
           
    else:
        if sum == num:
            result.append(num)
print(result)
          
        
            



