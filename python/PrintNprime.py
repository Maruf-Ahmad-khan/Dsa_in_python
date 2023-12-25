def CheckPrime(n):
     for i in range(2, n):
          if n % i == 0:
               return False
     return True     

def main():
     n = int(input("Enter the value of n : \n"))
     print("The prime number is : \n")
     for i in range(2, n):
          is_Prime = CheckPrime(i)
          if is_Prime:
               print(i, "\n")
               
if __name__ == "__main__":
    main()