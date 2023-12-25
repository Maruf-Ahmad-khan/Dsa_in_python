# write a program to find the maximum element in a list
# This code will not be valid when the element in the list will be negative
data = [12,34,56,78,90,100]
maxi = 0
for num in data:
     if num > maxi:
          maxi = num
print("The maximum value is :", maxi)
data.reverse()
print("The reverse element is :", data)

# find maxi using inbuilt function
print("The maxi will be :", max(data))

# print the element using range function
for i in range(5):
     print(data[i+1])
     