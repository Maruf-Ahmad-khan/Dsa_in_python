def main():
     n = int(input('Enter the number : \n'))
     counter = 1
     print("Table is : \n")
     while counter < 11:
          number = counter * n
          print(number ,"*", counter, "=", number)
          counter += 1
if __name__ == "__main__":
     main()