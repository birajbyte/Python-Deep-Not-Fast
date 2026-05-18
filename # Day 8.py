# Day 8
# Check if a list is sorted without sort()
l = [3, 1, 4, 2, 5]
for i in range(len(l)-1):
   if l[i] > l[i+1]:
      print("not sorted")
      break
else:
      print("sorted")
        



