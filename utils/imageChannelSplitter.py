from PIL import Image
import numpy as np


def splitImagesAndSave(image_path):
    # Load the image
    img = Image.open(image_path)
    # Convert the image to a numpy array
    img_array = np.array(img)
    red, green, blue = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]
    # Create RGB images for each channel
    red_channel_img = Image.fromarray(
        np.stack([red, np.zeros_like(red), np.zeros_like(red)], axis=-1)
    )
    red_channel_img.save("red_channel_image.jpg")

    green_channel_img = Image.fromarray(
        np.stack([np.zeros_like(green), green, np.zeros_like(green)], axis=-1)
    )
    green_channel_img.save("green_channel_image.jpg")

    blue_channel_img = Image.fromarray(
        np.stack([np.zeros_like(blue), np.zeros_like(blue), blue], axis=-1)
    )
    blue_channel_img.save("blue_channel_image.jpg")
