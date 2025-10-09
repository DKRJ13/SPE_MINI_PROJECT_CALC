"""Command-line interface for the scientific calculator."""
from .calculator import sqrt, factorial ,ln, power

def print_menu():
    print("Scientific Calculator")
    print("1) Square root (√x)")
    print("2) Factorial (!x)")
    print("3) Natural logarithm ln(x)")
    print("4) Power x^b")
    print("5) Exit")


def run():
    while True:
        print_menu()
        choice = input("Choose an option: ")
        try:
            if choice == '1':
                x = float(input("Enter x: "))
                print(f"√{x} = {sqrt(x)}")
            elif choice == '2':
                n = int(input("Enter n (non-negative integer): "))
                print(f"{n}! = {factorial(n)}")
            elif choice == '3':
                x = float(input("Enter x (>0): "))
                print(f"ln({x}) = {ln(x)}")
            elif choice == '4':
                x = float(input("Enter x: "))
                b = float(input("Enter b: "))
                print(f"{x}^{b} = {power(x, b)}")
            elif choice == '5':
                print("Goodbye")
                break
            else:
                print("Invalid option")
        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    run()
