# solution_q5.py
from collections import deque

def find_path(graph, start, end):
    """Finds a path between start and end stations using Breadth-First Search (BFS)."""
    if start not in graph or end not in graph:
        return None # One of the stations doesn't exist

    # The queue will store paths (lists of stations)
    queue = deque([[start]])
    # A set to keep track of visited stations to avoid cycles
    visited = {start}

    while queue:
        path = queue.popleft()
        current_station = path[-1]

        if current_station == end:
            return path # Path found

        for neighbor in graph.get(current_station, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None # No path found

# Main script execution
if __name__ == "__main__":
    # The metro map is hardcoded as an adjacency list
    metro_graph = {
        'Tajrish': ['Gheytariyeh'],
        'Gheytariyeh': ['Tajrish', 'Mirdamad'],
        'Mirdamad': ['Gheytariyeh', 'Teatr'],
        'Sadeghiyeh': ['Teatr'],
        'Teatr': ['Sadeghiyeh', 'Mirdamad']
    }

    try:
        start_station, end_station = input().split()
        
        path = find_path(metro_graph, start_station, end_station)
        
        if path:
            print(" -> ".join(path))
        else:
            print("No path found!")
            
    except (ValueError, IndexError):
        print("Invalid input. Please enter start and end stations separated by a space.")