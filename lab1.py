def greet_user(name):
    """Greet the user with their name."""
    if not isinstance(name, str):
        raise ValueError("Name must be a string")
    print(f"Hello, {name}!")

def factorial(number):
    """Calculate the factorial of a number."""
    if not isinstance(number, int) or number < 0:
        raise ValueError("Number must be a non-negative integer")
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

def main():
    """Main function to demonstrate functionality."""
    try:
        greet_user("Alice")
        print("Factorial of 5:", factorial(5))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
