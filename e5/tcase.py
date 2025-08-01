import os

# Define the test cases for Question 5
# Input: "start_station end_station"
# Output: A -> B -> C path or "No path found!"
test_cases = [
    # Example 1: Simple path on one line
    ("Tajrish Mirdamad", "Tajrish -> Gheytariyeh -> Mirdamad"),

    # Example 2: Path requiring a transfer
    ("Gheytariyeh Sadeghiyeh", "Gheytariyeh -> Mirdamad -> Teatr -> Sadeghiyeh"),

    # Example 3: No path exists
    ("Tajrish Azadi", "No path found!"),

    # Test Case 4: Reverse path requiring a transfer
    ("Sadeghiyeh Tajrish", "Sadeghiyeh -> Teatr -> Mirdamad -> Gheytariyeh -> Tajrish"),

    # Test Case 5: Start and end stations are the same
    ("Teatr Teatr", "Teatr"),

    # Test Case 6: Path from an end-of-line to the transfer station
    ("Sadeghiyeh Mirdamad", "Sadeghiyeh -> Teatr -> Mirdamad"),
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

print("Test case folders for Question 5 created successfully!")