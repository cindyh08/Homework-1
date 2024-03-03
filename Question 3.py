# BootCamp Section 2 Question 3
# Write a function sum_of_integers(a,b) that takes two intgers as input from yhe user and returns the sum


def sum_of_integers(a, b):
    sum = a + b
    return sum


a = int(input("Enter your value for a: "))
b = int(input("Enter your value for b: "))
print("The sum of", a, "and", b, "is ", sum_of_integers(a, b))
