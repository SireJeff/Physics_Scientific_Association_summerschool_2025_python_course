# plot_data.py
import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "oscillator_data.csv"

def plot_oscillator_data():
    """Reads oscillator data from a CSV and plots it."""
    try:
        # 1. Use pandas to read the CSV file into a DataFrame
        data = pd.read_csv(FILENAME)
        print("Data loaded successfully. Plotting...")
        
        # 2. Use matplotlib to create the plot
        plt.figure(figsize=(10, 6)) # Create a figure with a nice size
        
        plt.plot(data['time'], data['position'], marker='o', linestyle='-', markersize=4)
        
        # 3. Add title and labels for clarity
        plt.title("Simple Harmonic Oscillator Motion")
        plt.xlabel("Time (s)")
        plt.ylabel("Position (m)")
        
        # Add a grid for better readability
        plt.grid(True)
        
        # 4. Display the plot
        plt.show()

    except FileNotFoundError:
        print(f"Error: {FILENAME} not found.")
        print("Please run generate_data.py first to create the data file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    plot_oscillator_data()