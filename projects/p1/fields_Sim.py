# Required libraries: pip install vpython numpy matplotlib
import vpython as vp
import numpy as np
import matplotlib.pyplot as plt

# --- Physical Constants ---
K_e = 8.99e9  # Coulomb's constant (N m^2 / C^2)

# --- Object-Oriented Structure for Charges ---

class Charge:
    """
    A class to represent an electric charge, handling both its
    physical properties and its 3D visual representation in VPython.
    """
    def __init__(self, q, pos):
        """
        Initializes a charge.
        q: Charge in Coulombs (e.g., 10e-6 for 10 microcoulombs).
        pos: A vpython.vector for the (x, y, z) position.
        """
        self.q = q
        self.pos = pos
        
        # Determine radius using a logarithmic scale for better visualization
        # This formula prevents errors for q=0 and scales nicely.
        # C1 (base radius) + C2 * log(abs(q)/1e-9 + 1)
        self.radius = 0.1 + 0.05 * np.log10(abs(self.q) / 1e-9 + 1)

        # Determine color based on charge sign
        self.color = vp.color.red if self.q > 0 else vp.color.blue

        # Create the 3D sphere object for VPython
        self.sphere = vp.sphere(pos=self.pos, radius=self.radius, color=self.color)
        # Add a label to show the charge value
        self.label = vp.label(pos=self.pos, text=f"{self.q*1e6:.1f} μC", 
                              xoffset=20, yoffset=12, space=self.radius)

# --- Physics Calculation Functions ---

def calculate_net_efield(charges, obs_pos):
    """
    Calculates the net electric field at a given observation position
    due to a list of charges, using the superposition principle.
    """
    E_net = vp.vector(0, 0, 0)
    for charge in charges:
        r_vec = obs_pos - charge.pos
        r_mag = vp.mag(r_vec)
        
        # Avoid division by zero if the observation point is on a charge
        if r_mag < 1e-6:
            continue
            
        r_hat = vp.norm(r_vec)
        E_field = (K_e * charge.q / r_mag**2) * r_hat
        E_net += E_field
        
    return E_net

# --- Main Simulation and Visualization Functions ---

def visualize_3d_field(charge_objects):
    """
    Sets up and runs the VPython 3D simulation.
    """
    # 1. Setup the scene
    vp.canvas(title="Electric Field Simulation", width=1000, height=800,
              center=vp.vector(0, 0, 0), background=vp.color.gray(0.2))
    
    # 2. Define a grid of points to visualize the field
    grid_range = 5
    grid_step = 1.0
    points = [vp.vector(x, y, z) 
              for x in np.arange(-grid_range, grid_range + grid_step, grid_step)
              for y in np.arange(-grid_range, grid_range + grid_step, grid_step)
              for z in np.arange(-grid_range, grid_range + grid_step, grid_step)]
    
    # 3. Calculate and draw the E-field vectors (arrows)
    # A scaling factor is needed to make the arrows visible but not too large
    E_scale = 0.5 / (K_e * 1e-6 / grid_step**2) 

    for point in points:
        E_vector = calculate_net_efield(charge_objects, point)
        E_magnitude = vp.mag(E_vector)
        
        if E_magnitude > 0:
            # Map magnitude to color (blue for weak, red for strong)
            arrow_color = vp.vector(min(1, E_magnitude/1e7), 0, max(0.5, 1 - E_magnitude/1e7))
            
            vp.arrow(pos=point, 
                     axis=E_scale * E_vector, 
                     color=arrow_color)

def plot_field_vs_distance(charge_objects):
    """
    Generates a 2D plot of E-field magnitude vs. distance from a charge.
    """
    # Use the first charge as the reference for the plot
    ref_charge = charge_objects[0]
    
    # Generate a range of distances
    distances = np.linspace(ref_charge.radius * 2, 10, 200)
    E_magnitudes = []
    
    for r in distances:
        # Calculate E-field at a point 'r' distance away along the x-axis
        obs_point = ref_charge.pos + vp.vector(r, 0, 0)
        E_net = calculate_net_efield(charge_objects, obs_point)
        E_magnitudes.append(vp.mag(E_net))
        
    # Create the plot using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(distances, E_magnitudes, label='Net E-Field Magnitude')
    
    # Plot the theoretical 1/r^2 curve for the reference charge for comparison
    theoretical_E = [K_e * abs(ref_charge.q) / r**2 for r in distances]
    plt.plot(distances, theoretical_E, 'r--', label=f'Theoretical Field from {ref_charge.q*1e6:.1f} μC charge')
    
    plt.title("Electric Field Strength vs. Distance")
    plt.xlabel("Distance from reference charge (m)")
    plt.ylabel("E-Field Magnitude (N/C)")
    plt.yscale('log') # Log scale is often better for 1/r^2 plots
    plt.legend()
    plt.grid(True)
    plt.show()


# --- Main Execution Block ---
if __name__ == "__main__":
    # Define the charges for the simulation (Level 1: a simple dipole)
    # You can add more charges here for the Level 2 implementation
    charges_to_simulate = [
        {'q': 10e-6, 'pos': vp.vector(-1, 0, 0)},  # 10 μC positive charge
        {'q': -10e-6, 'pos': vp.vector(1, 0, 0)}    # -10 μC negative charge
        # {'q': 5e-6, 'pos': vp.vector(0, 2, 0)} # Example of adding a third charge
    ]
    
    # Create Charge objects from the data
    charge_instance_list = [Charge(q=c['q'], pos=c['pos']) for c in charges_to_simulate]

    # Run the 3D visualization
    # This will open a new browser tab with the 3D scene
    print("Starting VPython 3D visualization...")
    visualize_3d_field(charge_instance_list)

    # Generate and display the 2D plot
    # This will open a Matplotlib window
    print("\nGenerating 2D plot of E-Field vs. Distance...")
    plot_field_vs_distance(charge_instance_list)