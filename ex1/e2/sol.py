# solution_q2.py

def calculate_kinetic_energy(mass, velocity):
    """Calculates kinetic energy using the formula KE = 0.5 * m * v^2."""
    return 0.5 * mass * (velocity ** 2)

# Main script execution
if __name__ == "__main__":
    try:
        # Read the line and split it into two parts
        parts = input().split()
        m = float(parts[0])
        v = float(parts[1])
        
        ke = calculate_kinetic_energy(m, v)
        print(ke)
    except (ValueError, IndexError):
        print("Invalid input. Please enter mass and velocity separated by a space.")