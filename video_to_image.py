from cvs import *
import cv2
from utils import process_points


cap = cvs.VideoCapture("/home/lesson5_codes/aidlux/video.mp4")
frame_id = 0
while True:
    frame = cap.read()
    if frame is None:
        continue
    points = [[593,176],[904,243],[835,323],[507,259]]
    lines=[[186,249],[1235,366]]
    color_light_green=(144, 238, 144)  
    res_img=cv2.line(frame,[186,249],[1235,366],color_light_green,3)
    cvs.imshow(res_img)


    