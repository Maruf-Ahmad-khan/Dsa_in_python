# print reversed pyramid pattern
n = int(input("Enter the value of n : \n"))
# print the row 
for row in range(n):
     # print the spaces
     for col in range(row):
          print(" ", end= "")
          # print the star
     for col in range(n - row):
          print(" *", end="")
     print()