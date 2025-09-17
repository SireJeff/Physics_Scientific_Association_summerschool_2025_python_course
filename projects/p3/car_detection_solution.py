# Required libraries: pip install opencv-python matplotlib
import cv2
import matplotlib.pyplot as plt
import os

def detect_and_display_cars(image_path, cascade_path):
    """
    Detects cars in an image using a Haar Cascade classifier and displays the result.

    Args:
        image_path (str): The path to the input image file.
        cascade_path (str): The path to the Haar Cascade XML file.
    """
    # --- 1. Load the Image and Classifier ---

    # Check if the cascade file exists before trying to load it
    if not os.path.exists(cascade_path):
        print(f"Error: Cascade file not found at '{cascade_path}'")
        print("Please download 'haarcascade_car.xml' and place it in the same folder as the script.")
        return

    # Load the pre-trained Haar Cascade classifier for cars
    car_cascade = cv2.CascadeClassifier(cascade_path)

    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at '{image_path}'")
        print("Please provide an image with cars named 'test_image.jpg' or update the path.")
        return

    # Read the input image from the specified path
    image = cv2.imread(image_path)
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Could not read the image from '{image_path}'. The file may be corrupted or in an unsupported format.")
        return

    # --- 2. Perform Detection ---

    # Convert the image to grayscale, as Haar Cascades work on grayscale images
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use the detectMultiScale method to find cars.
    # These parameters can be tuned for better accuracy on different images.
    # - scaleFactor: How much the image size is reduced at each image scale.
    # - minNeighbors: How many neighbors each candidate rectangle should have to be retained.
    cars = car_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    print(f"Found {len(cars)} car(s) in the image.")

    # --- 3. Draw Bounding Boxes on the Original Image ---

    # Loop over all the coordinates of the detected cars
    for (x, y, w, h) in cars:
        # Draw a green rectangle on the original color image
        # cv2.rectangle(image, start_point, end_point, color, thickness)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

    # --- 4. Display the Final Image ---
    
    # OpenCV loads images in BGR format, but Matplotlib displays in RGB.
    # We need to convert the color channels for correct display.
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Display the image using Matplotlib
    plt.figure(figsize=(12, 8))
    plt.imshow(image_rgb)
    plt.title('Car Detection Result')
    plt.axis('off') # Hide the axes for a cleaner look
    plt.show()


# --- Main Execution Block ---
if __name__ == "__main__":
    # Define the path to the classifier XML file and the image you want to test.
    
    # You must download this file and place it in the same folder as the script.
    # Download link is in the project description.
    CASCADE_FILE_PATH = 'haarcascade_car.xml'
    
    # You need to provide your own image with cars to test the script.
    # Place it in the same folder and name it 'test_image.jpg', or change the path here.
    IMAGE_FILE_PATH = 'test_image.jpg' 

    detect_and_display_cars(image_path=IMAGE_FILE_PATH, cascade_path=CASCADE_FILE_PATH)