# write a program to create a list and find it's total sum
# using inbuilt function and without inbuilt function

data = [12,34,56,78,90]
total = 0
for num in data:
     total = total + num
print('The total sum of \'data\' is :', total)

# using inbuilt function
Sum = sum(data)
print('The total sum  of \'data \' is :', Sum)     