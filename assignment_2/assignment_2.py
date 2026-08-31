import cv2

def padding(image, border_width):
    padded_image = cv2.copyMakeBorder(
        image,
        border_width,
        border_width,
        border_width,
        border_width,
        cv2.BORDER_REFLECT
    )

    return padded_image

def crop(image, x_0, x_1, y_0, y_1):
    # ...
    return cropped_image

def resize(image, width, height):
    # ...
    return resized_image

def copy(image, emptyPictureArray):
    # ...
    return copied_image

def grayscale(image):
    # ...
    return grayscale_image

def hsv(image):
    # ...
    return hsv_image

def hue_shifted(image, emptyPictureArray, hue):
    # ...
    return hue_shifted_image

def smoothing(image):
    # ...
    return smoothed_image

def rotation(image, rotation_angle):
    # ...
    return rotated_image


def main():
    image = cv2.imread("iris-1.jpg")

    if image is None:
        print("Image Not Found")
        return

    padded_image = padding(image, 100)
    cv2.imwrite("solutions/padded_image.jpg", padded_image)


if __name__ == "__main__":
    main()

