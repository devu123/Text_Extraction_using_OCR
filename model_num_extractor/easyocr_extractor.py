import re
from logging import Logger
from typing import Optional

import cv2
import easyocr

from image_processing.image_processor import unskew
from model_num_extractor.extractor import extract_model_number_from_text

reader = easyocr.Reader(['en'])

rotations = [cv2.ROTATE_90_COUNTERCLOCKWISE, cv2.ROTATE_90_CLOCKWISE]


def easyocr_mn_extractor(img_src: str, logger: Logger, rotate_pic: bool = False) -> Optional[str]:
    img = cv2.imread(img_src)
    content = base_content_easyocr(img, logger)
    model_numbers = []
    mn = None
    if content is not None:
        if len(content.strip()) > 0:
            mn = extract_model_number_from_text(content, logger)
    if mn is not None:
        model_numbers.append(mn)
    if rotate_pic:
        for i in range(2):
            rotated_content = rotated_content_easyocr(img, rotations[i], logger)
            new_mn = None
            if rotated_content is not None:
                if len(rotated_content.strip()) > 0:
                    new_mn = extract_model_number_from_text(rotated_content, logger)
            if new_mn is not None:
                model_numbers.append(new_mn)
    if len(model_numbers) == 0:
        logger.info(f"Unable to find text in image <{img_src}>.")
        return None
    return max(model_numbers, key=len).upper()


def rotated_content_easyocr(img, rotation, logger) -> str:
    rotated_img = cv2.rotate(img, rotation)
    img = unskew(rotated_img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    adaptive = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 4)
    content = reader.readtext(adaptive)
    txt = ' '.join([i[1] for i in content])
    logger.info(f"Extracted text: <{txt}>")
    multiple_spaces_removed_txt = re.sub("\s+|\n", " ", txt)
    logger.info(f"Extracted text without multiple spaces: <{multiple_spaces_removed_txt}>")
    return multiple_spaces_removed_txt


def base_content_easyocr(img, logger) -> str:
    # EasyOCR work best without these image pre-processing
    # img = unskew(img)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    # adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 4)
    content = reader.readtext(img)
    txt = ' '.join([i[1] for i in content])
    logger.info(f"Extracted text: <{txt}>")
    multiple_spaces_removed_txt = re.sub("\s+|\n", " ", txt)
    logger.info(f"Extracted text without multiple spaces: <{multiple_spaces_removed_txt}>")
    return multiple_spaces_removed_txt
