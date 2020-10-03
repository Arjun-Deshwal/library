import cv2
from random import randrange
# Giving it the trained data 
trained_data=cv2.CascadeClassifier('h_f_d.xml')
path=input('Enter the path of the image with it\'s extension:')
img=cv2.imread(path)

# converting it into grayscale so that we can get its coordinates
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# getting the face coordinates from gray scale images
face_cordinates=trained_data.detectMultiScale(gray_img)
print(face_cordinates)

# drawing ractagle along the coordinates on the colored image
for i in range(len(face_cordinates)):
    x,y,w,h=face_cordinates[i]
    cv2.rectangle(img,(x,y),(w+x,h+y),(randrange(256),randrange(256),randrange(256)),2)

#showing the colored image    
cv2.imshow('My image',img)
cv2.waitKey()
print('Task completed sir!')
