# Document-Scanner
This is a repository that is aimed to help you work around on a computer vision project which is a document scanner using OpenCV.

## The codebase

### requiremnts.txt
1.  Opencv - python
2.  numpy
3.  imutils

### scanner.py
This python file takes the input from the user in the form of the image to be scanned and provides the scanned binary image as the output.
Necessary comments have been added for simplification of the code, but for further reference https://docs.opencv.org/4.x/index.html is a very good place to visit.

Words of Caution: To get a clean and market worthy scan please use a contrast background from the image. This helps in creating the edges of the document properly which is the backbone of this algorithm.
