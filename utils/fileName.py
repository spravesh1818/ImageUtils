import os


def outputFilePath(path):
    base_output_dir_path = "output"
    output_file_with_extension = path.split("/")[-1]

    filename = base_output_dir_path + "/" + output_file_with_extension

    return filename


def getFileStats(path):
    file_stats = os.stat(path)

    file_size_in_mb = file_stats.st_size / (1024 * 1024)

    return file_size_in_mb
