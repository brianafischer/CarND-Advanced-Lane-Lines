import pickle
import numpy as np
import glob
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

tf_img = cv2.imread('output_images/straight_lines1_undistort.jpg')

height, width = tf_img.shape[:2]

src = np.float32([(722, 470),
                  (1110, 720),
                  (220, 720),
                  (570, 470)])

dst = np.float32([(920, 100),
                  (920, 720),
                  (320, 720),
                  (320, 100)])

# dst = np.float32([(1000, 430),
#                  (1000, 690),
#                  (250,  690),
#                  (250,  430)])

# Plot our source transform using OpenCV polylines function
# https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
pts = src.astype(np.int32)
pts = pts.reshape((-1, 1, 2))

cv2.polylines(tf_img, [pts], True, (255, 255, 0), thickness=3)
plt.imshow(cv2.cvtColor(tf_img, cv2.COLOR_BGR2RGB))
plt.title('Source Transform')

M = cv2.getPerspectiveTransform(src, dst)
M_inv = cv2.getPerspectiveTransform(dst, src)
img_size = (tf_img.shape[1], tf_img.shape[0])

warped = cv2.warpPerspective(tf_img, M, (width, height), flags=cv2.INTER_LINEAR)

f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7))
f.tight_layout()
ax1.imshow(cv2.cvtColor(tf_img, cv2.COLOR_BGR2RGB))
ax1.plot(920, 100, 'x', color='red')
print(dst[1])
ax1.plot(dst[1], 'x', color='red')
ax1.set_title('Original Image')
ax2.imshow(warped, cmap='gray')
ax2.set_title('Warped Image')
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)