import cv2
import imutils
import numpy as np
import pytesseract
 
import tkinter.filedialog                           #
from tkinter import Tk                              #
                                                    # Deschide fisierul preferat
tkinter.Tk().withdraw()                             #
filename = tkinter.filedialog.askopenfilename()     #
 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #Deschidem tesseract
img = cv2.imread(filename) #Poza pe care o alegem
#img = cv2.resize(img, (800, 600)) #Micsoram chenarul cu poza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Aplicam un filtru monocrom pe imagine
cv2.imshow("img1", gray) #Afisam imaginea
 
gray = cv2.bilateralFilter(gray,25,25,25) #Aplicam un filtru mat
cv2.imshow("img1", gray) #Afisam imaginea
edged = cv2.Canny(gray,55,200) #Evidentiem conturul
cv2.imshow("img1", edged) #Afisam imaginea
 
contur=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE) #Detectare contur
contur = imutils.grab_contours(contur)
contur = sorted(contur,key=cv2.contourArea,reverse=True)[:10]
screenCnt = None
for c in contur:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.018*peri,True)
    if(len(approx)==4):
        screenCnt = approx
        break
if screenCnt is None:
    detected = 0
    print("nu am gasit niciun contur")
else:
    detected = 1
 
mask = np.zeros(gray.shape,np.uint8) #Creem o masca
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1)
cv2.imshow("img1",new_image) #Afisam noua imagine
new_image = cv2.bitwise_and(img,img,mask=mask) #Aplicam masca asupra imaginii initiale
cv2.imshow("img1",new_image)
(x,y)=np.where(mask==255) 
 
(topx,topy) = (np.min(x),np.min(y))
(bottomx,bottomy) = (np.max(x),np.max(y))
Crop = gray[topx:bottomx+1,topy:bottomy+1]
Crop = cv2.add(Crop,np.array([-50.0]) , Crop)
Crop = cv2.multiply(Crop,np.array([1.25]),Crop)
text_numar = pytesseract.image_to_string(Crop,config ='--psm 10')
 
img = cv2.resize(img, (500,300))
Crop = cv2.resize(Crop, (400,200))
cv2.imshow("img1",Crop)
print(text_numar)
cv2.waitKey(0)
cv2.destroyAllWindows()