import cv2
import numpy as np

# Load the image
image_path = 'C:/Users/shafa/Downloads/sport.jpg'
original_image = cv2.imread(image_path)

# Convert the image to the HSV color space (Hue, Saturation, Value)
hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds of the color you want to segment
lower_color = np.array([5, 100, 100], dtype=np.uint8)
upper_color = np.array([15, 255, 255], dtype=np.uint8)

# Create a binary mask based on the color range
color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Apply the mask to the original image
segmented_image = cv2.bitwise_and(original_image, original_image, mask=color_mask)

# Display the original and segmented images
cv2.imshow('Original Image', original_image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
