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
for row in range(n):
    # Print spaces
    for col in range(row):
        print(" ", end="")
    
    # Print stars
    for col in range(2 * n - (2 * row + 1)):
        if col == 0:
            # First character
            print("* ", end="")
        elif col == 2 * n - 2 * row - 2:
            # Last character
            print("* ", end="")
        else:
            print(" ", end="")
    
    print()
     