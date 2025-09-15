# solution_q3.py

import numpy as np
import scipy.interpolate as interp
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import heapq

# --- Part 1: Interpolation and Path Reconstruction ---

def reconstruct_path(incomplete_path):
    """Interpolates missing points in a path."""
    # Convert path to a numpy array for easier manipulation
    path_array = np.array(incomplete_path, dtype=object)
    
    # Get indices of known points
    known_indices = np.where(path_array[:, 1] != None)[0]
    
    # Separate x and y coordinates
    x_coords = np.array([p[0] for p in path_array[known_indices]], dtype=float)
    y_coords = np.array([p[1] for p in path_array[known_indices]], dtype=float)
    
    # Create interpolation functions
    interp_x = interp.interp1d(known_indices, x_coords, kind='cubic', fill_value="extrapolate")
    interp_y = interp.interp1d(known_indices, y_coords, kind='cubic', fill_value="extrapolate")
    
    # Generate the full path
    all_indices = np.arange(len(incomplete_path))
    full_path_x = interp_x(all_indices)
    full_path_y = interp_y(all_indices)
    
    return np.column_stack((full_path_x, full_path_y))

# --- Part 3: Dijkstra's Algorithm for Path Optimization ---

def euclidean_distance(p1, p2):
    """Calculates the Euclidean distance between two points."""
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def dijkstra(nodes, start_node_idx, end_node_idx):
    """Finds the shortest path in a complete graph of nodes using Dijkstra's."""
    num_nodes = len(nodes)
    distances = {i: float('inf') for i in range(num_nodes)}
    distances[start_node_idx] = 0
    previous_nodes = {i: None for i in range(num_nodes)}
    
    # Priority queue stores (distance, node_index)
    pq = [(0, start_node_idx)]
    
    while pq:
        dist, current_idx = heapq.heappop(pq)
        
        if dist > distances[current_idx]:
            continue
        
        if current_idx == end_node_idx:
            break # Reached the destination

        # In a complete graph, every node is a neighbor
        for neighbor_idx in range(num_nodes):
            if neighbor_idx == current_idx:
                continue
            
            weight = euclidean_distance(nodes[current_idx], nodes[neighbor_idx])
            new_dist = distances[current_idx] + weight
            
            if new_dist < distances[neighbor_idx]:
                distances[neighbor_idx] = new_dist
                previous_nodes[neighbor_idx] = current_idx
                heapq.heappush(pq, (new_dist, neighbor_idx))
                
    # Reconstruct the path from end to start
    path = []
    current = end_node_idx
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    
    return path[::-1] # Return the reversed path

# --- Main Execution ---

if __name__ == "__main__":
    incomplete_path_data = [
        (0, 1), (1, 3), (2, 5), (3, 6), (4, None), 
        (5, 7), (6, 8), (7, None), (8, 10), (9, 11), 
        (10, 10.5), (11, None), (12, 8), (13, 6), 
        (14, 5), (15, None), (16, 2), (17, 1)
    ]

    # Perform Part 1
    full_path = reconstruct_path(incomplete_path_data)
    print("Path reconstructed successfully.")
    
    # --- Part 2: Visualization and Simulation ---
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title("Reconstructed Particle Path (Animation)")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")
    ax.plot(full_path[:, 0], full_path[:, 1], 'g--', alpha=0.5, label='Interpolated Path')
    particle, = ax.plot([], [], 'bo', markersize=10, label='Particle')
    ax.legend()
    ax.grid(True)
    ax.set_xlim(np.min(full_path[:,0]) - 1, np.max(full_path[:,0]) + 1)
    ax.set_ylim(np.min(full_path[:,1]) - 1, np.max(full_path[:,1]) + 1)

    def animate(i):
        particle.set_data(full_path[i, 0], full_path[i, 1])
        return particle,
    
    # Note: Animation might not display in all environments. A static plot is always shown.
    # ani = animation.FuncAnimation(fig, animate, frames=len(full_path), interval=100, blit=True)
    print("Displaying static plot of the reconstructed path...")
    plt.show()

    # --- Perform Part 3 ---
    print("\nCalculating shortest path using Dijkstra's algorithm...")
    start_idx, end_idx = 0, len(full_path) - 1
    shortest_path_indices = dijkstra(full_path, start_idx, end_idx)
    
    if shortest_path_indices and shortest_path_indices[0] == start_idx:
        print("Shortest path found.")
        shortest_path_coords = full_path[shortest_path_indices]
        
        # Visualize the result
        plt.figure(figsize=(10, 8))
        plt.plot(full_path[:, 0], full_path[:, 1], 'g--', alpha=0.4, label='Interpolated Path')
        plt.plot(shortest_path_coords[:, 0], shortest_path_coords[:, 1], 'r-o', linewidth=2, markersize=5, label="Dijkstra's Shortest Path")
        plt.plot(full_path[start_idx, 0], full_path[start_idx, 1], 'go', markersize=15, label='Start')
        plt.plot(full_path[end_idx, 0], full_path[end_idx, 1], 'ro', markersize=15, label='End')
        
        plt.title("Path Optimization with Dijkstra's Algorithm")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.legend()
        plt.grid(True)
        print("Displaying plot of the optimized path...")
        plt.show()
    else:
        print("Could not find a path with Dijkstra's algorithm.")