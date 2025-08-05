# ------------------- Constants -------------------
PI = 3.141592653589793
E = 2.718281828459045

# ------------------- Basic Arithmetic -------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus by zero is not allowed.")
    return a % b

# ------------------- Advanced Functions -------------------
def power(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    elif int(b) == b:
        result = 1
        for _ in range(int(b)):
            result *= a
        return result
    else:
        return exponential(b * logarithm(a))

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    if a == 0:
        return 0
    x = a
    for _ in range(20):  
        x = (x + a / x) / 2
    return x

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def exponential(x):
    result = 1.0
    term = 1.0
    for i in range(1, 30):
        term *= x / i
        result += term
    return result

def logarithm(a, base=E):
    if a <= 0:
        raise ValueError("Logarithm only defined for positive numbers.")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base for logarithm.")

    n = 0.0
    while a >= base:
        a /= base
        n += 1
    a -= 1
    result = a
    term = a
    for i in range(2, 30):
        term *= -a
        result += term / i
    return n + result

# ------------------- Trigonometric Functions (Radians) -------------------
def sin_func(x, radians=False):
    if not radians:
        x = deg_to_rad(x)
    x %= 2 * PI
    result = 0
    term = x
    for i in range(1, 20, 2):
        result += term
        term *= -x * x / ((i + 1) * (i + 2))
    return result

def cos_func(x, radians=False):
    if not radians:
        x = deg_to_rad(x)
    x %= 2 * PI
    result = 0
    term = 1
    for i in range(0, 20, 2):
        result += term
        term *= -x * x / ((i + 1) * (i + 2))
    return result

def tan_func(x, radians=False):
    if not radians:
        x = deg_to_rad(x)
    return sin_func(x, True) / cos_func(x, True)

# ------------------- Angle Conversion -------------------
def deg_to_rad(angle):
    return angle * (PI / 180)

def rad_to_deg(angle):
    return angle * (180 / PI)

# ------------------- Number System Conversion -------------------
def decimal_to_binary(n):
    return bin(n)

def decimal_to_octal(n):
    return oct(n)

def decimal_to_hexadecimal(n):
    return hex(n)

def binary_to_decimal(b):
    return int(b, 2)

def octal_to_decimal(o):
    return int(o, 8)

def hexadecimal_to_decimal(h):
    return int(h, 16)

# ------------------- Show Constants -------------------
def show_constants():
    print(f"π (pi) ≈ {PI}")
    print(f"e (Euler's number) ≈ {E}")

# ------------------- Menu -------------------
def main():
    while True:
        print("\n=== Scientific Calculator ===")
        print("1. Basic Arithmetic")
        print("2. Advanced Math Functions")
        print("3. Trigonometric Functions")
        print("4. Number System Conversions")
        print("5. Angle Conversions")
        print("6. Show Constants")
        print("0. Exit")

        choice = input("Select an option: ")

        try:
            if choice == '1':
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Choose operation: +, -, *, /, %")
                op = input("Operation: ")
                if op == '+': print("Result:", add(a, b))
                elif op == '-': print("Result:", subtract(a, b))
                elif op == '*': print("Result:", multiply(a, b))
                elif op == '/': print("Result:", divide(a, b))
                elif op == '%': print("Result:", modulus(a, b))
                else: print("Invalid operation.")

            elif choice == '2':
                print("1. Power\n2. Square Root\n3. Factorial\n4. Exponential\n5. Logarithm")
                sub = input("Choose function: ")
                if sub == '1':
                    a = float(input("Base: "))
                    b = float(input("Exponent: "))
                    print("Result:", power(a, b))
                elif sub == '2':
                    a = float(input("Number: "))
                    print("Result:", square_root(a))
                elif sub == '3':
                    n = int(input("Number: "))
                    print("Result:", factorial(n))
                elif sub == '4':
                    a = float(input("Number: "))
                    print("Result:", exponential(a))
                elif sub == '5':
                    a = float(input("Number: "))
                    base = input("Base (default e): ")
                    if base == "":
                        print("Result:", logarithm(a))
                    else:
                        print("Result:", logarithm(a, float(base)))

            elif choice == '3':
                print("1. sin  2. cos  3. tan")
                func = input("Choose: ")
                angle = float(input("Enter angle: "))
                rad = input("Is it in radians? (y/n): ").lower() == 'y'
                if func == '1':
                    print("Result:", sin_func(angle, rad))
                elif func == '2':
                    print("Result:", cos_func(angle, rad))
                elif func == '3':
                    print("Result:", tan_func(angle, rad))
                else:
                    print("Invalid choice.")

            elif choice == '4':
                print("1. Decimal to Binary/Octal/Hex")
                print("2. Binary/Octal/Hex to Decimal")
                sub = input("Choose: ")
                if sub == '1':
                    n = int(input("Enter decimal number: "))
                    print("Binary:", decimal_to_binary(n))
                    print("Octal:", decimal_to_octal(n))
                    print("Hexadecimal:", decimal_to_hexadecimal(n))
                elif sub == '2':
                    print("1. Binary\n2. Octal\n3. Hexadecimal")
                    t = input("Choose type: ")
                    val = input("Enter value: ")
                    if t == '1':
                        print("Decimal:", binary_to_decimal(val))
                    elif t == '2':
                        print("Decimal:", octal_to_decimal(val))
                    elif t == '3':
                        print("Decimal:", hexadecimal_to_decimal(val))
                    else:
                        print("Invalid type.")

            elif choice == '5':
                print("1. Degrees to Radians")
                print("2. Radians to Degrees")
                sub = input("Choose: ")
                angle = float(input("Enter angle: "))
                if sub == '1':
                    print("Radians:", deg_to_rad(angle))
                elif sub == '2':
                    print("Degrees:", rad_to_deg(angle))
                else:
                    print("Invalid choice.")

            elif choice == '6':
                show_constants()

            elif choice == '0':
                print("Thank you for using the Scientific Calculator!")
                break
            else:
                print("Invalid choice.")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    main()
