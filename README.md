# Text Extraction using OCR

This repository is to hold the modules for optical character recognition and extraction of model number from images of appliances.
___
`accuracy_test_on_entire_dataset_using_pytesseract.ipynb` and `accuracy_test_on_entire_dataset_using_easyocr.ipynb` are
two jupyter notebooks that use pytesseract and easyocr libraries respectively for extracting text from images and locate model number for that extracted text.

In each notebook there is `predict_mn()` function where image rotation can be set in `rotate_pic` parameter.
If it is set to `True`, text extraction happens three times and every other time the image is rotated 90 degrees from the previous one.
The rotation that gives the longest non-whitespace string is taken as the correct orientation and eventually the correct text extraction.

Rotating an image on each run slightly improves the predicting capability but significantly decreases the computation - O(n).

---

_The maintainers of this repository are Deval Shah and Roby Rai

---
