def ncalc():
    print('Welcome to dxcalc standard mode.')
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
def nbmi():
    print('Welcome to dxcalc BMI calculator.')
    w = float(input('Enter your weight (kg): '))
    h = float(input('Enter your height (cm): '))
    def bmicalc():
        bmi = w / ((h / 100) * (h / 100))
        return bmi
    bmi = bmicalc()
    print('Your BMI is: ',bmi)
    if bmi < 18.5:
        print('You are underweight.')
    elif bmi < 25:
        print('You are average.')
    elif bmi < 30:
        print('You are overweight.')
    else:
        print('You are obese.')
print('''Welcome to dxcalc v2.
The license information is in the license tab on the calculator.''')
mode = input('''
Select a mode to continue
1. Standard Calculator
2. BMI Calculator
(1/2): ''')
if mode == '1':
    ncalc()
if mode == '2':
    nbmi()
