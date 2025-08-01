# solution_q4.py

# Main script execution
if __name__ == "__main__":
    try:
        n = int(input())
        
        # Use a list comprehension with nested conditional (ternary) operators
        fizzbuzz_list = [
            'FizzBuzz' if i % 15 == 0 
            else 'Fizz' if i % 3 == 0 
            else 'Buzz' if i % 5 == 0 
            else str(i) 
            for i in range(1, n + 1)
        ]
        
        # Join the list elements with a space for the final output
        print(" ".join(fizzbuzz_list))
        
    except (ValueError, IndexError):
        print("Invalid input. Please enter a single positive integer.")