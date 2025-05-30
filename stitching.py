from matplotlib import pyplot as plt
import cv2 as cv
from stitching import Stitcher

def plot_image(img, figsize_in_inches=(5,5)):
    fig, ax = plt.subplots(figsize=figsize_in_inches)
    ax.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
    plt.show()

stitcher = Stitcher(detector="sift", confidence_threshold=0.2)
panorama = stitcher.stitch(["imatge?.jpg"])
plot_image(panorama, (20,20))
