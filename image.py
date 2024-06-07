# import cv2
# import numpy as np

# # Load the image
# image_path = 'img2.jpg'
# image = cv2.imread(image_path)

# # Convert the image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Apply GaussianBlur to reduce noise and improve edge detection
# blurred = cv2.GaussianBlur(gray, (5,5), 0)  # Adjust this value if needed

# # Apply Canny edge detection
# edges = cv2.Canny(blurred, 50, 150)  # Adjust these values if needed

# # Find contours in the edged image
# contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# # Find the bounding box of the largest contour
# largest_contour = max(contours, key=cv2.contourArea)
# x, y, w, h = cv2.boundingRect(largest_contour)

# # Crop the region of interest
# cropped_image = image[y:y+h, x:x+w]

# # Save the cropped image
# cv2.imwrite('extracted_region.jpg', cropped_image)

# # Display the cropped image
# cv2.imshow('Cropped Image', cropped_image)

# # Display the intermediate steps for debugging
# cv2.imshow('Grayscale Image', gray)
# cv2.imshow('Blurred Image', blurred)
# cv2.imshow('Edge Detection', edges)

# # Wait for a key press and close the windows
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2
import numpy as np

def process_image(image_path, roi_size=(100, 100)):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the center of the image
    center_x, center_y = width // 2, height // 2

    # Calculate the coordinates of the ROI
    roi_width, roi_height = roi_size
    x1 = max(center_x - roi_width // 2, 0)
    y1 = max(center_y - roi_height // 2, 0)
    x2 = min(center_x + roi_width // 2, width)
    y2 = min(center_y + roi_height // 2, height)

    # Create a blank canvas to hold the result
    result = np.zeros_like(image)

    # Copy the grayscale ROI into the result image
    result[y1:y2, x1:x2] = cv2.cvtColor(gray[y1:y2, x1:x2], cv2.COLOR_GRAY2BGR)

    # Save the extracted region
    output_path = 'extracted_region.jpg'
    cv2.imwrite(output_path, result)

    # Display the extracted region
    cv2.imshow('Extracted Region', result)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'img6.jpg'
process_image(image_path, roi_size=(350, 300))  # Adjust roi_size as needed