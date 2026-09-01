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
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    return hsv_image

def hue_shifted(image, emptyPictureArray=None, hue=50):
    heigth, width, channels = image.shape

    if emptyPictureArray is None:
        emptyPictureArray = np.zeros((heigth, width, 3), dtype=np.uint8)

    for y in range(heigth):
        for x in range(width):
            for channel in range(channels):
                emptyPictureArray[y, x, channel] = (
                    int(image[y, x, channel]) + hue
                ) % 256
                #to stay within the 0-255 range

    return emptyPictureArray

def smoothing(image):
    smoothed_image = cv2.GaussianBlur(image, (15, 15), 0, borderType=cv2.BORDER_DEFAULT)
    return smoothed_image

def rotation(image, rotation_angle):
    if rotation_angle == 90:
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    elif rotation_angle == 180:
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)

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

    grayscale_image = grayscale(image)
    cv2.imwrite("solutions/grayscale_image.jpg", grayscale_image)

    hsv_image = hsv(image)
    cv2.imwrite("solutions/hsv_image.jpg", hsv_image)

    hue_shifted_image = hue_shifted(image, hue=50)
    cv2.imwrite("solutions/hue_shifted_image.jpg", hue_shifted_image)

    smoothed_image = smoothing(image)
    cv2.imwrite("solutions/smoothed_image.jpg", smoothed_image)

    rotated_image = rotation(image, 180)
    cv2.imwrite("solutions/rotated_image.jpg", rotated_image)


if __name__ == "__main__":
    main()

