
# License Plate Reader

This project is a license plate recognition system designed to detect and read Iranian car license plates using a laptop camera or webcam. It is implemented using the `OpenCV` and `pytesseract` libraries.

## Features
- Simultaneous detection of multiple license plates in an image.
- Drawing bounding boxes around detected plates and displaying extracted text.
- Support for Iranian license plates (combination of Persian letters and numbers).
- Real-time processing using a webcam.

## Prerequisites
To run this project, you need to install the following libraries and tools:

### 1. Install Tesseract-OCR
- **Windows:**
  1. Download and install the latest version of `Tesseract-OCR` from [here](https://github.com/UB-Mannheim/tesseract/wiki).
  2. Add the installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your system's `PATH` environment variable.
  3. Download the Persian language file (`fas.traineddata`) from [here](https://github.com/tesseract-ocr/tessdata) and place it in the `tessdata` folder.

- **Linux (Ubuntu):**
  ```bash
  sudo apt update
  sudo apt install tesseract-ocr
  sudo apt install libtesseract-dev
  ```

### 2. Install Python Libraries
The project uses the following Python libraries:
- `opencv-python`
- `pytesseract`
- `numpy`

Install them using the following commands:
```bash
pip install opencv-python pytesseract numpy
```

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/shahin-mansouri/license-plate-reader.git
   cd license-plate-reader
   ```

2. Run the `license_plate_reader.py` file:
   ```bash
   python license_plate_reader.py
   ```

3. The system will use your webcam to detect and read license plates in real-time.

## Project Structure
- `license_plate_reader.py`: The main script.
- `README.md`: Project documentation.
- `requirements.txt`: List of required libraries.

## Configuration
- If `Tesseract` is not installed in the default path, specify its path in the code:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

- To improve accuracy, you can adjust the parameters of `Canny` and `bilateralFilter` in the `detect_plates` function.



### Notes:
- You can edit the `README.md` file as needed.
- If you want to generate a `requirements.txt` file, use the following command:
  ```bash
  pip freeze > requirements.txt
  ```

This file is ready to be copied and pasted into your project. Let me know if you need further assistance! 😊
