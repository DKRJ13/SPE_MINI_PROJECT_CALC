"""Command-line interface for the scientific calculator."""
from .calculator import sqrt, factorial, ln, power
import sys
import time


def print_menu():
    print("Scientific Calculator")
    print("1) Square root (√x)")
    print("2) Factorial (!x)")
    print("3) Natural logarithm ln(x)")
    print("4) Power x^b")
    print("5) Exit")
    print("New feature")


def run():
    while True:
        print_menu()
        try:
            choice = input("Choose an option: ")
        except EOFError:
            # No TTY attached — switch to non-interactive mode to avoid crash loops
            print("No TTY detected; switching to non-interactive mode.")
            run_noninteractive()
            return

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


def run_noninteractive():
    """Minimal non-interactive wait loop used when no TTY is attached.

    Keeps the process alive so container orchestration doesn't repeatedly
    restart it when input() would raise EOFError.
    """
    # print("Running in non-interactive (container) mode. Waiting...", flush=True)
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    if not sys.stdin.isatty():
        # print("[startup] no TTY detected, entering non-interactive mode", flush=True)
        run_noninteractive()
    else:
        # print("[startup] interactive TTY detected, starting CLI", flush=True)
        run()

    #testing webhook

