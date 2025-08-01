# solution_q1.py

def factorial(n):
    """Calculates the factorial of a non-negative integer."""
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main script execution
if __name__ == "__main__":
    try:
        num = int(input())
        print(factorial(num))
    except (ValueError, IndexError):
        print("Invalid input. Please enter a single non-negative integer.")