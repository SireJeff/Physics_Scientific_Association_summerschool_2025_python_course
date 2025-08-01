import os

# Define the test cases: (input_content, output_content)
test_cases = [
    ("0", "1"),
    ("1", "1"),
    ("5", "120"),
    ("10", "3628800"),
    ("13", "6227020800"),
    ("20", "2432902008176640000"),
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

print("Test case folders 'in' and 'out' created successfully!")