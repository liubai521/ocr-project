# -*- coding: utf-8 -*-

from ocr.cropimage import trimmed_image, pad_and_resize


def showimg(img):
    """Just display an image."""
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def imgfile_to_grayscale(filename, resize=None):
    """Load an image file as grayscale."""
    assert os.path.isfile(filename)
    img = cv2.imread(filename, 0)
    if resize:
        trimmed = trimmed_image(img)
        img = pad_and_resize(trimmed, resize, resize)
    return img

