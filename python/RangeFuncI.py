# Very Important 
print(range(9))
print(range(0,9))
print(list(range(9)))
print(list(range(1, 10,1)))
print(list(range(10, 12, -2)))
print(list(range(10, 0, -2)))
print(list(range(5, 1)))
for i in range(-1, 10, 2):
     print(i, end=' ')
print()
print(i)
for i in range(6):
     print(i*i, end=' ')
print()
print(i)

sum = 0
for i in range(-1, 10, 2):
     sum = sum + i
print()
print(sum)

n = int(input("Enter n : \n"))
i = 1
for i in range(i, n+1):
     print(i, end= ' ')
print()

# print all odd integer from 1 to N using for loop
num = int(input("Enter number : \n"))
j = 1
for j in range(j, num + 1, 2):
     print(j)
print()

# print N number of stars in a sequence
N = int(input("Enter N : \n"))
counter = 1
for counter in range(counter, N + 1, 1):
     print("*", end = " ")
print()