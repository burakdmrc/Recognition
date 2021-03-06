# -*- coding: utf-8 -*-
"""FaceRecognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E8i5EvSkdji0CrWAbBoQ32M4IlLvFZZg
"""

!apt update
!apt install cmake
!pip install dlib

!pip install face_recognition

!wget https://www.alastyr.com/blog/wp-content/uploads/2020/08/bill-gates.jpg
!wget https://muhendislik.sdu.edu.tr/assets/uploads/sites/46/other/28798.jpg

import numpy as np
from PIL import Image, ImageDraw
import face_recognition

def load_image( infilename ) :
    img = Image.open( infilename )
    img.load()
    data = np.asarray(img, dtype="int32")
    return data

im=face_recognition.load_image_file("bill-gates.jpg")
im2=face_recognition.load_image_file("28798.jpg")

face_locations=face_recognition.face_locations(im)
face_locations2=face_recognition.face_locations(im2)

e1=face_recognition.face_encodings(im) [0]
e2=face_recognition.face_encodings(im2) [0]

print(e1.shape)
print(e2.shape)

result=face_recognition.compare_faces([e1],e2)

print (result)
(top, right,bottom,left)=face_locations[0]
(top2, right2,bottom2,left2)=face_locations2[0]

pil_image = Image.fromarray(im)

draw=ImageDraw.Draw(pil_image)

draw.rectangle(((left,top),(right,bottom)), outline=(0,255,255))

pil_image

pil_image = Image.fromarray(im2)

draw=ImageDraw.Draw(pil_image)

draw.rectangle(((left2,top2),(right2,bottom2)), outline=(0,255,255))

pil_image