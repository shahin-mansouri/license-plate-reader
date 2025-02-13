import cv2
import numpy as np


def multi_scale_template_matching(main_img, template, scales=np.arange(0.5, 1.2, 0.1)):
    """
    Perform multi-scale template matching on the main image using the provided template.
    Returns a list of detected regions with their corresponding scores.
    """
    detected = []
    for scale in scales:
        resized_template = cv2.resize(template, None, fx=scale, fy=scale)
        h, w = resized_template.shape

        # Skip if the resized template is larger than the main image
        if h > main_img.shape[0] or w > main_img.shape[1]:
            continue

        res = cv2.matchTemplate(main_img, resized_template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.8)

        for pt in zip(*loc[::-1]):
            detected.append((pt[0], pt[1], pt[0] + w, pt[1] + h, res[pt[1], pt[0]]))
    return detected


def non_max_suppression_fast(boxes, scores, overlapThresh=0.3):
    """
    Remove overlapping regions based on the Intersection over Union (IoU) criteria.
    Returns indices of the boxes to keep.
    """
    if len(boxes) == 0:
        return []

    boxes = np.array(boxes).astype("float")
    scores = np.array(scores)

    pick = []
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]

    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = np.argsort(scores)

    while len(idxs) > 0:
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        overlap = (w * h) / area[idxs[:last]]

        idxs = np.delete(
            idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0]))
        )

    return pick


def preprocess_image(image):
    """
    Reduce noise and enhance contrast of the image using CLAHE.
    Returns the preprocessed image.
    """
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(blurred)


# Load and preprocess the main image (in grayscale)
main_img = cv2.imread("img.png", 0)
if main_img is None:
    raise Exception("Main image not found!")
main_img = preprocess_image(main_img)

detected_boxes = []
detected_scores = []
detected_digits = []

# Process digits 0 to 9
for digit in range(0, 10):
    template = cv2.imread(f"numbers/{digit}.png", 0)
    if template is None:
        continue

    template = preprocess_image(template)
    detections = multi_scale_template_matching(main_img, template)

    for (x1, y1, x2, y2, score) in detections:
        detected_boxes.append([x1, y1, x2, y2])
        detected_scores.append(score)
        detected_digits.append(digit)

# Apply non-maximum suppression to remove overlapping detections
indices = non_max_suppression_fast(detected_boxes, detected_scores)
final_results = sorted(
    [(detected_boxes[i], detected_digits[i]) for i in indices],
    key=lambda x: (x[0][0], x[0][1])  # Sort by x coordinate then y coordinate
)

# Convert main image to BGR for color drawing
output_img = cv2.cvtColor(main_img, cv2.COLOR_GRAY2BGR)
for box, digit in final_results:
    x1, y1, x2, y2 = box
    cv2.rectangle(output_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(
        output_img,
        str(digit),
        (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2,
    )

# Perform corner detection for visual feedback
corners = cv2.goodFeaturesToTrack(main_img, maxCorners=200, qualityLevel=0.01, minDistance=10)
if corners is not None:
    corners = np.int64(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(output_img, (x, y), 3, (0, 0, 255), -1)

cv2.imshow("Final Result", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Detected digit sequence:", [digit for (_, digit) in final_results])
