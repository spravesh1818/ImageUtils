# Image Utils

This is a repository currently for learning purposes and is still a work in progress.The objective of this repository mostly to learn the techniques image processing and how they work internally.I have currently explored SVD and PCA here.Additionally I am trying to study the channels of the image.I have mostly stayed away from any use of libraries that directly implement these algorithm,PCA from scikit-learn being an exception as it was just used for comparison purposes.Here is the list of libraries used:

- numpy: For all numerical and matrix operations
- os: Built in package for managing files and folders
- matplotlib: For plotting and analysing by visualizations(Currently unused)
- PIL: Library to read and save image data(Before and after processing)

# Using the methods

## Installing the dependencies

To install the dependencies first create a virtual environment.Then go ahead and run

```
pip install -r requirements.txt
```

## Running the code

Currently just add the path of the file in the method in the main.py file.Working on a cli for this:

```
compress_image_pca_using_svd("./assets/sample2.jpg")
```

Just change the path of the image.Then run the code using:

```python
python main.py
```

# Future Enhancement and Plans

- Add other statistical analysis methods to be added for blurring,filtering,edge detections and study them
- Try to implement everything from scratch
- Add deep learning to the library.Mostly try and make creation of CNNs a breeze and from scratch
