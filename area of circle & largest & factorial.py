# factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example
num = 5
print("Factorial of", num, "is", factorial(num))

# largest number
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example
numbers = [10, 25, 67, 3, 99, 34]
print("Largest number is:", find_largest(numbers))

# area of circle
import math

def area_circle(radius):
    return math.pi * radius * radius

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

# Examples
print("Area of Circle (r=5):", area_circle(5))
print("Area of Rectangle (l=10, w=4):", area_rectangle(10, 4))
print("Area of Triangle (b=6, h=3):", area_triangle(6, 3))
