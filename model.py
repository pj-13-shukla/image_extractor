import cv2
from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO('best_Square.pt')  # Update the path to your best.pt file

# Function to detect and extract squares
def detect_and_extract_square(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    # Perform detection
    results = model(image)

    # Check if there are any detections
    if len(results) > 0:
        # Iterate through the detections
        for result in results:
            for bbox in result.boxes:
                # Get the bounding box coordinates
                x_min, y_min, x_max, y_max = map(int, bbox.xyxy[0])

                # Extract the detected square region
                square_region = image[y_min:y_max, x_min:x_max]

                # Save the extracted region
                cv2.imwrite(output_path, square_region)

                # Optionally, draw the bounding box on the original image
                cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

        # Display the original image with bounding boxes
        cv2.imshow('Detected Squares', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("No squares detected.")

# Provide the path to the image you want to process
input_image_path = 'img1.jpg'  # Replace with the path to your input image
output_image_path = 'extracted_square.jpg'  # Replace with the desired output path

# Call the function to detect and extract the square
detect_and_extract_square(input_image_path, output_image_path)
