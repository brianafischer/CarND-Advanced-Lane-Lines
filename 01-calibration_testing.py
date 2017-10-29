import pickle
import numpy as np
import glob
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# List all calibration image names
images = glob.glob('camera_cal/calibration*.jpg')
current_dir = os.getcwd()

img = cv2.imread(images[0])
print("Calibration Image Shape:", img.shape)
plt.imshow(img)
print("Calibration Image Aspect Ratio:", img.shape[1]/img.shape[0])

# Define the number of corners
nx = 9   # horizontal corners
ny = 6   # vertical corners

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((nx*ny,3), np.float32)
objp[:,:2] = np.mgrid[0:nx, 0:ny].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d points in real world space
imgpoints = [] # 2d points in image plane.

# List all calibration image names
images = glob.glob('camera_cal/calibration*.jpg')

img = cv2.imread(images[0])
aspect_ratio = img.shape[1]/img.shape[0]

# Setup the plot
fig, axes = plt.subplots(4,5, figsize=(16*aspect_ratio,16))
axes = axes.ravel()

# Step through the list and search for chessboard corners
for idx, fname in enumerate(images):
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (nx,ny), None)

    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (nx,ny), corners, ret)
        axes[i].axis("off")
        axes[i].imshow(img)


