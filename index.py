import 

# Load the OCR reader with the English language model
reader = easyocr.Reader(['en'])

# Load the image
image_path = '/workspaces/python/IMG_20231207_1gfdsg22355.jpg'

# Use easyocr to do OCR on the image
result = reader.readtext(image_path)

# Print the extracted text
if result:
    print("Extracted Text:")
    for detection in result:
        print(detection[1])  # Extracted text
else:
    print("No text found in the image.")
