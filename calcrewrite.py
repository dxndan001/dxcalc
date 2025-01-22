while True:
    import time
    def ncalc():
        while True:
            print("Standard Mode")
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            op = input("Enter operation (+, -, *, /,): ")
            time.sleep(1)
            if op == "+":
                res = first + second
                print(float(res))
            elif op == "-":
                res = first - second
                print(float(res))
            elif op == "*":
                res = first * second
                print(float(res))
            elif op == "/":
                res = first / second
                print(float(res))
            else:
                print("input a valid operation")
            ta = input("Do you still want to use the calculator (y/n): ")
            if ta == "n":
                print("Thanks for using the Standard mode.")
                break
            elif ta == "y":
                continue
    def bmi():
        while True:
            print("Welcome to BMI Mode")
            print("Please note that this calculator is optimised for adults.")
            print("There might be differences between this calculator and")
            print("other calculators when calculating kids' or teenagers' BMI.")
            w = float(input("Enter your weight in kilograms: "))
            h = float(input("Enter your height in centimetres: ")) ** 2
            bmi = w / h * 10000
            print(bmi)
            if bmi < 18.5:
                print("Category: Underweight")
            elif bmi < 25:
                print("Category: Average")
            elif bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")
            ta = input("Do you still want to use the calculator (y/n): ")
            if ta == "n":
                print("Thanks for using the BMI mode.")
                break
            elif ta == "y":
                continue
    def about():
        while True:
            print("dxcalc Rewrite 2025 edition, Copyright (c) Danish Narendra.")
            print("dxcalc Rewrite 2025 edition is licensed under the MIT License.")
            print("For more information, please check the GitHub page.")
            print("https://github.com/dxndan001/dxcalc")
            b = input("Press enter to go back ")
            if b == (""):
                break
            else:
                break
    print("Welcome to dxcalc rewrite.")
    print(" 1. Standard Mode")
    print(" 2. BMI Calculator (ALPHA)")
    print(" 3. About")
    print(" 4. Exit")
    mode = input("Select the desired mode by their number to continue: ")
    if mode == "1":
        ncalc()
    elif mode == "2":
        bmi()
    elif mode == "4":
        break
    elif mode == "3":
        about()