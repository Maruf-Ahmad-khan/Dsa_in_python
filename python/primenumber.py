def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input("Enter the value of n: "))
    is_prime = check_prime(n)
    
    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")

if __name__ == "__main__":
    main()
