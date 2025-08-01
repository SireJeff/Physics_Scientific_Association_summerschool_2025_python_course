import os

# Define the test cases for Question 3
# Input: base-10 number
# Output: line 1 = binary, line 2 = hexadecimal
test_cases = [
    ("0", "0\n0"),
    ("10", "1010\nA"),
    ("26", "11010\n1A"),
    ("255", "11111111\nFF"),
    ("482", "111100010\n1E2"),
    ("1000000", "11110100001001000000\nF4240"),
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

print("Test case folders for Question 3 created successfully!")