n = int(input("Enter a number :\n"))
count = 0

while n > 0:
     rem = n % 10
     print(rem)
     n = n // 10
     count = count + 1
print("The digits are : \n",count)
          
          