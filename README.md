# Digit Recognition with Multi-scale Template Matching

This project implements a digit recognition system using multi-scale template matching with OpenCV. It processes an input image containing digits, applies noise reduction and contrast enhancement, and uses template matching to locate and recognize digits based on provided template images. The system also employs non-maximum suppression to filter overlapping detections and uses corner detection for visual feedback.

## Features

- **Preprocessing:** Reduces noise using Gaussian Blur and enhances contrast with CLAHE.
- **Multi-scale Template Matching:** Matches digit templates at various scales to handle different digit sizes.
- **Non-maximum Suppression:** Removes overlapping detections based on Intersection over Union (IoU) criteria.
- **Visualization:** Draws bounding boxes and digit labels on the detected regions and displays detected corner points.

## Requirements

- Python 3.x
- [OpenCV](https://opencv.org/) (`opencv-python`)
- [NumPy](https://numpy.org/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shahin-mansouri/license-plate-reader.git
   cd license-plate-reader


2. **Install the required packages:**

   ```bash
   pip install opencv-python numpy
   ```

## Project Structure

- **img.png:** Main input image containing digits.
- **numbers/:** Directory containing grayscale template images for digits (0-9).
- **main.py:** Python script implementing the digit recognition system.
- **README.md:** This file.

## Usage

1. **Prepare your images:**
   - Place your main image (`img.png`) in the repository root.
   - Ensure the `numbers/` directory contains template images for digits 0-9.

2. **Run the script:**

   ```bash
   python plate_image_reader2.py
   ```

3. **View the results:**
   - An output window will display the processed image with detected digits outlined and labeled.
   - The detected digit sequence will also be printed to the console.

## Configuration

You can adjust various parameters in `plate_image_reader2.py` to fine-tune detection:

- **Template Matching Threshold:** Modify the threshold in the `multi_scale_template_matching` function (default is set to `0.8`).
- **Scale Range:** Adjust the `scales` parameter (default is `np.arange(0.5, 1.2, 0.1)`) in the template matching function.
- **Non-maximum Suppression Threshold:** Change the `overlapThresh` value in the `non_max_suppression_fast` function.
- **Corner Detection Parameters:** Tweak parameters for `cv2.goodFeaturesToTrack` (e.g., `maxCorners`, `qualityLevel`, `minDistance`) to suit your image.

## Acknowledgements

- [OpenCV](https://opencv.org/) for the robust image processing tools.
- [NumPy](https://numpy.org/) for efficient numerical computations.
```

---

Feel free to modify any sections as needed to better suit your project's specifics.
