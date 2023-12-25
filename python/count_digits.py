# wrp to count the digits and calculate the sum of the digits
n = int(input("Enter n :\n"))
sum = 0
count = 0
while n > 0:
     rem = n % 10
     count = count + 1
     sum = sum + rem
     n = n // 10
print("Count the digits \n", count)
print("The sum is : \n", sum)