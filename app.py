from image_processing.image_processor import get_model_number_from_img_using_pytesseract
from logger import get_logger

logger = get_logger("app")


# you can play with the other helper functions from here
def main() -> None:
    src_path = "./data/SJ48703391/image-pre-inspection-serial-number-a1243346-87be-42b6-b861-644375f01073_4b38c7f8-fc0a-4f67-bd71-31813162631e.png"
    model_number = get_model_number_from_img_using_pytesseract(src_path, logger)
    print(f"model number = {model_number}")


if __name__ == '__main__':
    exit(main())
