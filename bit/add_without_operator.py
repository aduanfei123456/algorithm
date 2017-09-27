"""
The following code adds two positive integers without using the '+' operator.
The code uses bitwise operations to add two numbers.
Input: 2 3
Output: 5
"""
def addWithoutOperator(x,y):
    while y!=0:
        temp=x&y
        x=x^y
        y = temp << 1

    print(x)
