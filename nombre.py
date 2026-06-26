import pytesseract as tess
from PIL import Image
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#    img = Image.open(r'C:\Users\Administrador\OCR\dni.png')
img = cv2.imread(r'C:\Users\Administrador\OCR\dni.png')
txt = tess.image_to_string(img)
print(txt)

# cv2.imshow('image', img)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()

cv2.imshow('image', img)
cv2.waitKey(500)
cv2.destroyAllWindows()
print(txt)


my_file = open('file.txt', 'w')
my_file.write(txt + '\n')
my_file.close()