# solution_q2.py
import json
import os

class CustomizedList:
    """A list-like class that persists its data to a JSON file."""
    
    def __init__(self, filepath="list_data.json"):
        """Initializes the list, loading from the file if it exists."""
        self.filepath = filepath
        self._data = []
        self.load()

    def load(self):
        """Loads data from the JSON file into the internal list."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self._data = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                # If file is empty, corrupted, or can't be found, start fresh
                self._data = []
        else:
            self._data = []

    def dump(self):
        """Saves the internal list's data to the JSON file."""
        with open(self.filepath, 'w') as f:
            json.dump(self._data, f, indent=4)
        print(f"Data saved to {self.filepath}")

    # --- Dunder methods to mimic list behavior ---
    
    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        # This supports both indexing and slicing
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]
    
    def __str__(self):
        return str(self._data)
    
    def __repr__(self):
        return f"CustomizedList(filepath='{self.filepath}') -> {self._data}"

    # --- Standard list-like methods ---
    
    def append(self, item):
        self._data.append(item)

# --- Main execution to demonstrate functionality ---
if __name__ == "__main__":
    # --- Run 1: Create and modify the list ---
    print("--- First Run ---")
    my_list = CustomizedList("my_data.json")
    print(f"Initial list (may be empty or loaded from previous run): {my_list}")

    # Clear the list to start fresh for this demonstration
    my_list._data = [] 
    
    my_list.append(10)
    my_list.append("hello")
    my_list.append({'a': 1, 'b': 2})
    print(f"List after appending: {my_list}")
    
    # Modify the list
    my_list[1] = "world"
    del my_list[0]
    print(f"List after modification: {my_list}")
    
    # Save the final state to the disk
    my_list.dump()
    print("-" * 20)

    # --- Run 2: Demonstrate persistence ---
    print("\n--- Second Run (Simulated) ---")
    # A new instance is created, which should automatically load the saved data
    persistent_list = CustomizedList("my_data.json")
    print(f"Loaded list from file: {persistent_list}")
    print(f"Length of loaded list: {len(persistent_list)}")
    print(f"First item: {persistent_list[0]}")