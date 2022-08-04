import cv2
import numpy as np
from scipy.ndimage import interpolation as inter

rotations = [cv2.ROTATE_90_COUNTERCLOCKWISE, cv2.ROTATE_90_CLOCKWISE]


def rotate(img: str, degrees: int):
    assert degrees in ['90', '180', '270'], "Degrees must be one of these values [\"90\", \"180\", \"270\"]"
    rotate_code = {90: cv2.ROTATE_90_COUNTERCLOCKWISE,
                   180: cv2.ROTATE_180,
                   270: cv2.ROTATE_90_CLOCKWISE}
    return cv2.rotate(img, rotate_code[degrees])


def unskew(image, delta: int = 1, limit: int = 5):
    def determine_score(arr, angle):
        data = inter.rotate(arr, angle, reshape=False, order=0)
        histogram = np.sum(data, axis=1, dtype=float)
        score = np.sum((histogram[1:] - histogram[:-1]) ** 2, dtype=float)
        return histogram, score

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    scores = []
    angles = np.arange(-limit, limit + delta, delta)
    for angle in angles:
        histogram, score = determine_score(thresh, angle)
        scores.append(score)

    best_angle = angles[scores.index(max(scores))]

    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, best_angle, 1.0)
    corrected = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, \
                               borderMode=cv2.BORDER_REPLICATE)
    return corrected


def grayscale(img: str):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def adaptive_threshold(img: str):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 4)


def blur(img: str):
    return cv2.GaussianBlur(img, (3, 3), 0)


def dilate(img: str):
    return cv2.dilate(img, np.ones((1, 1), 'uint8'), 0)


def erode(img: str):
    return cv2.erode(img, np.ones((1, 1), 'uint8'), 0)


def process_img(img: str, *args):
    result = img
    for process in args:
        result = process(result)
    return result
