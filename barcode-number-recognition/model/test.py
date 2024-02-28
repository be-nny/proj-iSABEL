try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
import re
import cv2


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

extracted_text = pytesseract.image_to_string(Image.open('numbers.png'), lang="eng")
print(extracted_text)
# Filter out non-numeric characters using regular expressions
numbers = re.sub(r'\D', '', extracted_text)
print(numbers)

