import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
from .fileName import outputFilePath, getFileStats


def compress_image_pca_using_svd(image_path):
    # Load the image
    img = Image.open(image_path)

    # Show the initial file size in mb
    initial_file_stats_in_mb = getFileStats(image_path)
    print(f"Initial file size before compression:{initial_file_stats_in_mb}")

    # get width and height of the image
    width = img.width
    height = img.height

    # minimum value from height and width
    minComponent = min(height, width)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Split the image into RGB channels
    red, green, blue = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    # Apply Singular Value Decomposition (SVD) to each channel
    compressed_channels = []
    for channel in (red, green, blue):
        U, S, Vt = np.linalg.svd(channel, full_matrices=False)

        # Truncate SVD matrices to keep only the most important components
        U_truncated = U[:, :minComponent]
        S_truncated = np.diag(S[:minComponent])
        Vt_truncated = Vt[:minComponent, :]

        # Reconstruct the compressed channel
        compressed_channel = np.dot(U_truncated, np.dot(S_truncated, Vt_truncated))
        compressed_channels.append(compressed_channel)

    # Stack the compressed channels back into an RGB image
    compressed_img_array = np.stack(compressed_channels, axis=-1).astype(np.uint8)

    img = Image.fromarray(compressed_img_array)
    filename = outputFilePath(image_path)
    img.save(filename)

    # Show the final file size in mb
    final_file_stats_in_mb = getFileStats(filename)
    print(f"File file size after compression:{final_file_stats_in_mb}")

    return compressed_img_array


def compress_image_pca(image_path):
    # Load the image
    img = Image.open(image_path)

    # Show the initial file size in mb
    initial_file_stats_in_mb = getFileStats(image_path)
    print(f"Initial file size before compression:{initial_file_stats_in_mb}")

    # get width and height of the image
    width = img.width
    height = img.height

    # minimum value from height and width
    minComponent = min(height, width)

    # Convert the image to a numpy array
    img_array = np.array(img)

    # Split the image into RGB channels
    red, green, blue = img_array[:, :, 0], img_array[:, :, 1], img_array[:, :, 2]

    # Apply PCA to each channel
    compressed_channels = []
    for channel in (red, green, blue):
        pca = PCA(n_components=minComponent)
        compressed_channel = pca.fit_transform(channel)
        reconstructed_channel = pca.inverse_transform(compressed_channel)
        compressed_channels.append(reconstructed_channel)

    # Stack the compressed channels back into an RGB image
    compressed_img_array = np.stack(compressed_channels, axis=-1).astype(np.uint8)

    img = Image.fromarray(compressed_img_array)
    filename = outputFilePath(image_path)
    img.save(filename)

    # Show the final file size in mb
    final_file_stats_in_mb = getFileStats(filename)
    print(f"File file size after compression:{final_file_stats_in_mb}")

    return compressed_img_array
