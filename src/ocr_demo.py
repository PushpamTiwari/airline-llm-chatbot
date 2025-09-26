import pytesseract
from PIL import Image
import sys
import os

def run_ocr_demo(image_path="boarding_pass.png"):
    if not os.path.exists(image_path):
        print(f"Image not found at: {image_path}")
        return
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print("Extracted Text:", text)
    except Exception as e:
        print("Error during OCR:", e) 

if __name__ == "__main__":
    # Use command-line argument if provided
    image_path = sys.argv[1] if len(sys.argv) > 1 else "boarding_pass.png"
    run_ocr_demo(image_path)
