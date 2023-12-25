Celcius = float(input("Enter the Celcius Value : \n"))
Fahrenheit =  9/5 * Celcius + 32
print("The Fahrenheit value is :\n", Fahrenheit)


# Take two number from the keyboard and write a program to swap it
num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n"))
num1 , num2 = num2, num1
print("swapping number is :\n")
print("num1= ", num1)
print("num2= ", num2)

# Write a program to find the euclidean distance between two coordinates.
# Take both the coordinates from the user as input.
import math
x1 = int(input("Enter x1 value : \n"))
x2 = int(input("Enter x2 value :\n"))
y1 = int(input("Enter y1 value : \n"))
y2 = int(input("Enter y2 value :\n"))
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The distance between two points are : \n", distance)