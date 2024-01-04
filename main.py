import pytesseract
import cv2
from pytesseract import Output
import os


def main():
    image_path = input("Enter the path to the image file: ")
    confidence_threshold = int(input("Enter the confidence threshold (default is 60): ") or 60)

    img = load_image(image_path)
    resized_img = resize_image(img, width=800)
    data = extract_text_data(resized_img, confidence_threshold)
    draw_text_boxes(resized_img, data, confidence_threshold)
    lines = extract_text_lines(data)
    result = '\n\n'.join(lines)
    save_to_text_file(image_path, result)
    display_image_with_boxes(resized_img)


def load_image(image_path):
    return cv2.imread(image_path)


def resize_image(img, width):
    aspect_ratio = img.shape[1] / img.shape[0]
    height = int(width / aspect_ratio)
    return cv2.resize(img, (width, height))


def extract_text_data(img, confidence_threshold):
    return pytesseract.image_to_data(img, config=f'--psm 11 --oem 3', output_type=Output.DICT)


def draw_text_boxes(img, data, confidence_threshold):
    for i in range(len(data['text'])):
        conf = int(data['conf'][i])

        if conf > confidence_threshold:
            x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, data['text'][i], (x, y + h + 20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)


def extract_text_lines(data):
    lines = []
    prev_top = None

    for i in range(len(data['text'])):
        conf = int(data['conf'][i])

        if conf > 0:  # Filter out low-confidence results
            left, top, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
            text = data['text'][i]

            if text.strip():  # Skip empty text
                if prev_top is None or top - prev_top >= h:  # New line
                    lines.append(text)
                else:
                    lines[-1] += ' ' + text  # Append to the last line

                prev_top = top

    return lines


def save_to_text_file(image_path, text):
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_directory = 'Text'
    os.makedirs(output_directory, exist_ok=True)
    output_path = os.path.join(output_directory, f'{base_name}.txt')

    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(text)


def display_image_with_boxes(img):
    cv2.imshow('OCR Result - Press ESC to Close', img)

    # Add text overlay on the window
    overlay = img.copy()
    cv2.putText(overlay, 'Click ESC to close', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    alpha = 0.7
    cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0, img)

    key = cv2.waitKey(0)
    if key == 27:  # Close on ESC key
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
