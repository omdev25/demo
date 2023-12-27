from PIL import Image
import pytesseract
import cv2

# Set the path to the Tesseract executable (change this to the correct path on your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = '/workspaces/python/IMG_20231207_1gfdsg22355.jpg'
img = Image.open(image_path)

# Preprocess the image (optional)
# You may need to experiment with different pre-processing steps based on your images
img = img.convert('L')  # Convert to grayscale
img = img.point(lambda x: 0 if x < 128 else 255, '1')  # Binarize the image

# Use pytesseract to do OCR on the preprocessed image
text = pytesseract.image_to_string(img)

# Print the extracted text
print("Extracted Text:")
print(text)
