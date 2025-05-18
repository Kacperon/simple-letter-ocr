import cv2
import numpy as np
import pytesseract
from PIL import Image
import os

# Uncomment and set the Tesseract executable path if it's not in the system PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def predict_letter(image_path):
    """
    Predicts a single letter from an image.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        tuple: (predicted_letter, confidence)
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot read image: {image_path}")
    
    # Resize image for consistency
    height, width = image.shape[:2]
    new_height = 200
    new_width = int((new_height / height) * width)
    image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)
    
    # Convert to grayscale and apply thresholding
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    thresh = cv2.medianBlur(thresh, 3)
    
    # Tesseract configuration for recognizing a single uppercase letter
    config = '--psm 10 --oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ -c tessedit_class_miss_scale=0.8'
    
    # OCR processing
    data = pytesseract.image_to_data(thresh, config=config, output_type=pytesseract.Output.DICT)
    
    def process_ocr_result(i):
        text = data['text'][i].strip()
        if not text:
            return None
        letter = text[0].upper()
        conf = float(data['conf'][i]) / 100.0
        if conf <= 0.05:
            return None
        return letter, conf
    
    valid_results = list(filter(None, map(process_ocr_result, range(len(data['text'])))))
    
    if not valid_results:
        return None, 0.0
    
    best_letter, best_conf = max(valid_results, key=lambda x: x[1])
    return best_letter, best_conf

if __name__ == "__main__":
    image_path = 'obraz.jpg'
    
    try:
        letter, probability = predict_letter(image_path)
        print(f"Recognized letter: {letter}")
        print(f"Confidence: {probability:.4f}")
    except Exception as e:
        print(f"Error: {str(e)}")
