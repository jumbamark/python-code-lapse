""" Open CV -is a library designed to solve computer vision problems """
# computer vision - inter disciplinary field that deals with how computers can be  made to gain high level understanding
# from digital images or videos, the idea is to automate task that the human visual system can do

# Basic operations with open cv
import cv2
# gray scale(black and white) image (2D array) - for coloured image use 1 (will output a 3D array
img = cv2.imread("/home/mark/Downloads/Penguin.jpeg", 1)
print(img)

# kind of matrix
print(type(img))

# size of the image
print(img.shape)  # one channel since its not colored


# capturing video
import cv2
import time
video = cv2.VideoCapture(0)
check, frame = video.read()
time.sleep(3)
cv2.imshow("Capturing", frame)
cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()