print('''Welcome to dxcalc v1.0 remastered.
The license information is in the license tab on the calculator.''')
n1 = int(input("Enter a number: "))
n2 = int(input("Enter the second number: "))
op = input('''
1. Addition
2. Subtraction
3. Multiplication
4. Division
Select an operation: ''')
if op == '1':
    print(n1 + n2)
elif op == '2':
    print(n1 - n2)
elif op == '3':
    print(n1 * n2)
elif op == '4':
    print(n1 / n2)