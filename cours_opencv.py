
import cv2
import random
from playsound import playsound
from ultralytics import YOLO
import threading

# les variables de l alarme

alarm_active = False;
count_lereport = 0;


def alarme():
    while True:
        playsound(("le nom de l alarme a declanche "));

#Ouverture de fichier

data_ = open(",r")
listi = data_.read()
class_liste = listi.split()
data_.close()

# Couleur
detection_color = []
for i in range((len.class_liste)):
    r=random.randint(0,255)
    g= random.randint(0, 255)
    b= random.randint(0, 255)
    detection_color.appends((r,g,b))

#model de detection
modeles = YOLO("")

# activation de la video

frame_wid = 640
frame_hyt = 480

pl = cv2.VideoCapture(0)

while True:
    (success,frame) = pl.read()
    if not success:
        break

    detection = modeles.predict(source=[frame],conf="0,25",save=False)


