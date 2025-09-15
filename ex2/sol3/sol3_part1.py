# generate_data.py
import csv
import math

# 1. Define physical constants and simulation parameters
MASS = 0.5          # kg
SPRING_K = 2.0      # N/m
AMPLITUDE = 1.5     # m
PHASE = 0.0         # radians
OMEGA = math.sqrt(SPRING_K / MASS) # Angular frequency

TIME_START = 0
TIME_END = 20
TIME_STEP = 0.1
FILENAME = "oscillator_data.csv"

# 2. Prepare the data list
data_to_write = []
current_time = TIME_START

while current_time <= TIME_END:
    # Calculate position using the SHO formula
    position = AMPLITUDE * math.cos(OMEGA * current_time + PHASE)
    
    # Append the (time, position) pair to our data list
    data_to_write.append([current_time, position])
    
    current_time += TIME_STEP

# 3. Write the data to a CSV file
try:
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the header row
        writer.writerow(["time", "position"])
        # Write all the data rows
        writer.writerows(data_to_write)
    print(f"Successfully generated and saved data to {FILENAME}")
except IOError:
    print(f"Error: Could not write to file {FILENAME}")