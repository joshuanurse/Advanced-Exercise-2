# ==============================================================================
# Question 1: Multi-Step Arithmetic Operations
# ==============================================================================
import math

# Start with some base values
a = 5
b = 10
c = 7

# Add 3 to a using +=
a += 3

# Multiply b by 2 using *=
b *= 2

# Modulo c by 4 using %=
c %= 4

# Calculate the square root of (a^2 + b^2 + c^2)
result = math.sqrt(a**2 + b**2 + c**2)

# Print the final result rounded to 2 decimal places
print(f"Question 1 Result: {result:.2f}")


# ==============================================================================
# Question 2: Complex Conditional Evaluation
# ==============================================================================
# Input x, y, z
x = int(input("Enter integer x: "))
y = int(input("Enter integer y: "))
z = int(input("Enter integer z: "))

# Create conditions
is_even = x % 2 == 0
is_positive = y > 0
is_in_range = 10 <= z <= 50

# Create final_condition
all_conditions_met = is_even and is_positive and is_in_range

# Print final_condition
print(f"Are all conditions met? {all_conditions_met}")


# ==============================================================================
# Question 3: Grading with Adjustments
# ==============================================================================
# Input score from user
base_score = float(input("Enter your base score: "))

# Apply adjustments
adjusted_score = base_score + 5 - 10

# Clamp score between 0 and 100
final_score = min(max(0, adjusted_score), 100)

# Use if-elif-else to determine grade and print it
if final_score >= 90:
    grade = "A"
elif final_score >= 80:
    grade = "B"
elif final_score >= 70:
    grade = "C"
elif final_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Adjusted Final Score: {final_score}")
print(f"Assigned Grade: {grade}")


# ==============================================================================
# Question 4: Advanced Calculator
# ==============================================================================
# Input num1, num2
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Input operation
operation = input("Enter operation (+, -, *, /, %, **): ")

# Handle calculation and potential division/modulus by zero errors
try:
    if operation == "+":
        calc_result = num1 + num2
    elif operation == "-":
        calc_result = num1 - num2
    elif operation == "*":
        calc_result = num1 * num2
    elif operation == "/":
        calc_result = num1 / num2
    elif operation == "%":
        calc_result = num1 % num2
    elif operation == "**":
        calc_result = num1 ** num2
    else:
        calc_result = "Invalid operation"

    print(f"Calculator Result: {calc_result}")

except ZeroDivisionError:
    print("Error: Division or modulus by zero is not allowed.")
