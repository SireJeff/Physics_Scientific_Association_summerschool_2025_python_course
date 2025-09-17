from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

# --- Flask App Initialization ---
app = Flask(__name__)
# Configure Matplotlib for a non-GUI backend
plt.switch_backend('agg')

# --- Helper Functions for Parsing ---

def parse_matrix_string(matrix_str):
    """Converts a string from a textarea into a NumPy array."""
    try:
        rows = matrix_str.strip().split('\n')
        matrix = [list(map(float, row.strip().split())) for row in rows]
        np_matrix = np.array(matrix)
        # Check if the matrix is square for determinant calculation
        if np_matrix.shape[0] != np_matrix.shape[1]:
            return None, "Error: Matrix must be square to calculate a determinant."
        return np_matrix, None
    except ValueError:
        return None, "Error: Invalid input. Please ensure all values are numbers and rows have the same length."
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"

def parse_plot_data(data_str):
    """Converts a two-column string into x and y numpy arrays for plotting."""
    try:
        x, y = [], []
        rows = data_str.strip().split('\n')
        for row in rows:
            parts = list(map(float, row.strip().split()))
            if len(parts) == 2:
                x.append(parts[0])
                y.append(parts[1])
        return np.array(x), np.array(y), None
    except ValueError:
        return None, None, "Error: Invalid data format. Please provide two columns of numbers."
    except Exception as e:
        return None, None, f"An unexpected error occurred: {e}"


# --- Flask Routes ---

@app.route('/')
def index():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/matrix', methods=['GET', 'POST'])
def matrix_calculator():
    """Handles the matrix calculator page."""
    matrix_input = "1 2\n3 4" # Default example
    results = {}
    error = None

    if request.method == 'POST':
        matrix_input = request.form.get('matrix_data', '')
        matrix, error = parse_matrix_string(matrix_input)
        
        if error is None:
            # Perform calculations
            results['determinant'] = np.linalg.det(matrix)
            results['transpose'] = matrix.T

    return render_template('matrix.html', matrix_input=matrix_input, results=results, error=error)

@app.route('/plotter', methods=['GET', 'POST'])
def data_plotter():
    """Handles the data plotting page."""
    plot_data_input = "1 1\n2 4\n3 9\n4 16" # Default example
    plot_url = None
    error = None

    if request.method == 'POST':
        plot_data_input = request.form.get('plot_data', '')
        x, y, error = parse_plot_data(plot_data_input)
        
        if error is None and x.size > 0 and y.size > 0:
            # Create plot
            plt.figure(figsize=(8, 6))
            plt.plot(x, y, marker='o', linestyle='-')
            plt.title("User Data Plot")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid(True)
            
            # Save plot to a memory buffer
            img = io.BytesIO()
            plt.savefig(img, format='png', bbox_inches='tight')
            img.seek(0)
            plt.close() # Important to close the plot to free up memory

            # Encode buffer to Base64 and pass to the template
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    return render_template('plotter.html', plot_data_input=plot_data_input, plot_url=plot_url, error=error)

# --- Main Execution Block ---
if __name__ == '__main__':
    app.run(debug=True)