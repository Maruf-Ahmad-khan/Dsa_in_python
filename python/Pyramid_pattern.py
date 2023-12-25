# pyramid pattern
n = int(input("Enter the value of n : \n"))
for row in range(n):
     # printing space n - row - 1
     for col in range(n - row - 1):
          print(" ", end = "")
     # printing number of stars row + 1 
     for col in range(row + 1):
          print(" *", end= "")
     print()