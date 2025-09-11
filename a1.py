# Assignment 1: AI-Generated Python Problems
# Name: [Aylish Irizarry]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[i need help learning python for my computer science class. I have no experience with python , so Can you create 5-7 practice problems that cover functions]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
[Write a function greet that takes a name as input and prints “Hello, [name]!”
Example: greet("Alice") should print Hello, Alice!



Create a function add that takes two numbers and returns their sum.
Example: add(3, 5) should return 8.



Write a function is_even that returns True if a number is even, otherwise False.
Example: is_even(4) returns True, is_even(7) returns False.




Define a function square that takes a number and returns its square (number multiplied by itself).
Example: square(6) returns 36.






Write a function print_countdown that takes a number n and prints numbers from n down to 1.
Example: print_countdown(3) prints:]



Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")

def greet(name):
    print(f"Hello, {name}!") 

greet("Aylish")

print("\nTesting Problem 2:")
def add(a, b):
    return a + b

print(add(6, 7))

print("\nTesting Problem 3:")
def is_even(num):
    return num % 2 == 0

print(is_even(3))

print("\nTesting Problem 4:")
def square(num):
    return num * num

print(square(6))

print("\nTesting Problem 5:")
def print_countdown(n):
    for i in range(n, 0, -1):
        print(i)
        
print_countdown(7)
