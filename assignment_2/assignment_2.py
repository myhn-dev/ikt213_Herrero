import cv2
import numpy as np

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
    cropped_image = image[y_0:y_1, x_0:x_1]
    return cropped_image

def resize(image, width, height):
    resized_image = cv2.resize(image, (width, height))
    return resized_image

def manual_copy(image, emptyPictureArray=None):
    #get dimensions:
    height, width, channels = image.shape

    #create blank image:
    if emptyPictureArray is None:
        emptyPictureArray = np.zeros((height, width, 3), dtype=np.uint8)

    #nested loops to copy each pixel from iris image to it:
    for y in range(height):
        for x in range(width):
            emptyPictureArray[y, x] = image[y, x]

    return emptyPictureArray

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

    cropped_image = crop(image, 200, -130, 200, -130)
    cv2.imwrite("solutions/cropped_image.jpg", cropped_image)

    resized_image = resize(image, 200, 200)
    cv2.imwrite("solutions/resized_image.jpg", resized_image)

    copied_image = manual_copy(image)
    cv2.imwrite("solutions/manual_copied_image.jpg", copied_image)




if __name__ == "__main__":
    main()

