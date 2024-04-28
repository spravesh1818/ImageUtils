from utils.compressImage import compress_image_pca_using_svd
import os


# Initially create output directory
os.mkdir("./output")


if __name__ == "__main__":
    compress_image_pca_using_svd("./assets/sample2.jpg")
