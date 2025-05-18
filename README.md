# 🧠 Letter Detector – Offline AI Letter Recognition from Images

This project recognizes single alphabet letters (A–Z) from `.jpg` images using a local AI model. It runs entirely offline and uses a pretrained Convolutional Neural Network (CNN) in `.h5` format via TensorFlow.

---

## 🔍 What It Does

- ✅ Detects a single letter from an input image (e.g., a handwritten or printed character).
- ✅ Runs completely offline — no internet connection required.
- ✅ Returns both the predicted letter and the confidence score.
- ✅ Automatically processes the input (resizes, normalizes, inverts colors).

---

## 🤖 Model Used

This project uses a pretrained model: `emnist_v7.h5`, created and shared by [zmandyhe](https://github.com/zmandyhe/image-classification-mnist-emnist-letters), trained on the [EMNIST Letters dataset](https://www.nist.gov/itl/products-and-services/emnist-dataset).

📁 Direct model download:  
🔗 https://github.com/zmandyhe/image-classification-mnist-emnist-letters/raw/master/emnist_v7.h5

---

## 🛠 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
