import pytesseract
from PIL import Image

def run_ocr_demo(image_path="boarding_pass.png"):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print("Extracted Text:", text)
    except FileNotFoundError:
        print("Sample image not found. Please provide a boarding_pass.png")

if __name__ == "__main__":
    run_ocr_demo()
