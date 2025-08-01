import os

# Define the test cases for Question 4
# Input: A single integer N
# Output: A space-separated FizzBuzz sequence from 1 to N
test_cases = [
    ("15", "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"),
    ("3", "1 2 Fizz"),
    ("5", "1 2 Fizz 4 Buzz"),
    ("2", "1 2"),
    ("1", "1"),
    ("20", "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz"),
]

# Create the 'in' and 'out' directories
os.makedirs("in", exist_ok=True)
os.makedirs("out", exist_ok=True)

# Loop through the test cases and create the files
for i, (input_data, output_data) in enumerate(test_cases, 1):
    # Create input file
    with open(os.path.join("in", f"input{i}.txt"), "w") as f:
        f.write(input_data)

    # Create output file
    with open(os.path.join("out", f"output{i}.txt"), "w") as f:
        f.write(output_data)

print("Test case folders for Question 4 created successfully!")