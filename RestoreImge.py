import cv2
import numpy as np

OriginalImage = cv2.imread("abraham.jpg")

# Resize the original image to fit in a single row of screen
resized_original_image = cv2.resize(OriginalImage, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Resized Original Image", resized_original_image)

makredDamages = cv2.imread("mask.jpg",0) # gray scale

# Resize the makredDamages image to fit in a single row of screen
resized_makred_damages = cv2.resize(makredDamages, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Resized makred Damages", resized_makred_damages)

# lets create a mask with threshhold
ret , thresh = cv2.threshold(makredDamages, 254, 255 , cv2.THRESH_BINARY)

# Resize the threshold image to fit in a single row of screen
resized_thresh = cv2.resize(thresh, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Resized mask threshold", resized_thresh)

# lets make the lines thicker
kernel = np.ones((7,7), np.uint8)
mask = cv2.dilate(thresh , kernel , iterations=1)

# Resize the mask image to fit in a single row of screen
resized_mask = cv2.resize(mask, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Resized mask", resized_mask)

# lets restore the image
restoredImage = cv2.inpaint(OriginalImage , mask , 3, cv2.INPAINT_TELEA)

# Resize the restoredImage image to fit in a single row of screen
resized_restored_image = cv2.resize(restoredImage, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Resized restored Image", resized_restored_image) 
cv2.imwrite("Restore-Damaged-Photo/RestoredAbraham.jpg",resized_restored_image)

cv2.waitKey(0)

cv2.destroyAllWindows() 