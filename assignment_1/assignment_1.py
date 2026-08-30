import cv2

def print_image_information(image):
    height, width, channels = image.shape

    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)
    print("Size:", image.size)
    print("Data Type:", image.dtype)

def main():
        image = cv2.imread("iris-1.jpg")

        if image is None:
            print("Could not load image")
            return

        print_image_information(image)

if __name__ == "__main__":
    main()