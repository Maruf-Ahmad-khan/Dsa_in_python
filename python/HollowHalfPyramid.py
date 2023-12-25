n = int(input("Enter the value of n : \n"))
for row in range(n):
     # print spaces
     for col in range(n - row - 1):
          print(" ", end="")
     # print stars
     for col in range(2 * row + 1):
     # print first character
       if col == 0 or col == 2 * row:
          print(" *",end="")
       else:
          print(" ", end="")
     print()