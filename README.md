# SimpleOCR

This is a simple Optical Character Recognition (OCR) script written in Python using Tesseract and OpenCV. It extracts text from images and displays the results with bounding boxes.

## Prerequisites

- [Python](https://www.python.org/) (version 3.6 or higher)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)

## Setup

1. Install the required Python libraries:

    ```bash
    pip install pytesseract opencv-python
    ```

2. Install Tesseract OCR. Refer to the [official Tesseract installation guide](https://github.com/tesseract-ocr/tesseract) for detailed instructions.

## Usage

1. Place your images in the `Images` directory.

2. Run the script by executing the following command:

    ```bash
    python SimpleOCR.py
    ```

3. Follow the prompts to enter the path to the image file and set the confidence threshold.

4. The script will display the image with bounding boxes around recognized text and save the extracted text in the `Text` directory.

## Configuration

- You can adjust the default confidence threshold by modifying the `confidence_threshold` variable in the script.

- The script resizes images to a fixed width (default is 800). You can change this value in the `resize_image` function.

## License

