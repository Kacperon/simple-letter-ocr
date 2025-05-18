# 🧠 Letter Detector – Offline OCR Letter Recognition from Images

This project recognizes single alphabet letters (A–Z) from `.jpg` images using Tesseract OCR. It runs entirely offline and processes images to extract letters with confidence scores.

---

## 🔍 What It Does

- ✅ Detects a single letter from an input image (e.g., a handwritten or printed character).
- ✅ Runs completely offline — no internet connection required.
- ✅ Returns both the predicted letter and the confidence score.
- ✅ Automatically processes the input (resizes, normalizes, thresholds).

---

## 🛠️ Technology Used

This project uses Tesseract OCR with Python:

- **OpenCV** - For image processing and preparation
- **Pytesseract** - Python wrapper for Google's Tesseract OCR engine
- **NumPy** - For numerical operations
- **PIL** - Python Imaging Library for additional image handling

## 📋 Installation

1. Install Tesseract OCR:
   - **Windows**: Download from [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
   - **Linux**: `sudo apt install tesseract-ocr`
   - **macOS**: `brew install tesseract`

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
