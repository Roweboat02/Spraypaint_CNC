from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def open_image(path):
    return Image.open(path)


def image_to_numpy_array(image):
    return np.asarray(image)


def numpy_image_to_greyscale(im_array):
    return np.mean(im_array[:,:,0:3], axis=-1)


def scale_to_white_to_black(im_array):
    a = (im_array-255)/-255
    a[a == np.NZERO] = 0
    return a


def show_image(im_array):
    plt.figure()
    plt.imshow(im_array, cmap='gray')
    plt.show()


if __name__ == "__main__":
    b = scale_to_white_to_black(
            numpy_image_to_greyscale(
                    image_to_numpy_array(
                            open_image("example_image_5.png"))))

    show_image(b)
