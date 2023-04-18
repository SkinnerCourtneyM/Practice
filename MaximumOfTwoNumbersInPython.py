# Python Practice: Maximum of two numbers in Python: 4/16/2023

# Example 1:
# Input: a = 2, b = 4
# Output: 4

# Python program to find the maximum of two numbers:

# def: Defining a Function in Python.

# Python program to find the
# maximum of two numbers


def maximum(a, b):

    if a >= b:
        return a
    else:
        return b


# Driver code
a = 2
b = 4
print(maximum(a, b))

# Python program to find the maximum of two numbers

# Driver code
a = 2
b = 4

# Use of ternary operator (Ternary Operator: An operator that taks the operands rather than the typical two)
print(a if a >= b else b)


# Python program to find the maximum of two numbers
#The Sort Method:
#The sort(Function) rturns a sorted List of specified iterable Objects:
a = 2
b = 4
x=[a,b]
x.sort()
print(x[-1])