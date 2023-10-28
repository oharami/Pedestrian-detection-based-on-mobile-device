# aidlux
from cvs import *
import aidlite_gpu
from utils import detect_postprocess, preprocess_img, draw_detect_res

import time
import cv2

aidlite = aidlite_gpu.aidlite()
model_path = '/pedestriandetection/yolov5n_best-fp16.tflite'
in_shape = [1 * 640 * 640 * 3 * 4]
out_shape = [1 * 25200 * 6 * 4]
aidlite.ANNModel(model_path, in_shape, out_shape, 4, 0)

cap = cvs.VideoCapture("/pedestriandetection/video2.mp4")
frame_id = 0
while True:
    frame = cap.read()
    if frame is None:
        continue
    frame_id += 1
    if not int(frame_id) % 5 == 0: continue
    img = preprocess_img(frame, target_shape=(640, 640), div_num=255, means=None, stds=None)
    aidlite.setInput_Float32(img, 640, 640)
    aidlite.invoke()
    pred = aidlite.getOutput_Float32(0)
    pred = pred.reshape(1, 25200, 6)[0]
    pred = detect_postprocess(pred, frame.shape, [640, 640, 3], conf_thres=0.5, iou_thres=0.45)
    res_img = draw_detect_res(frame, pred)
    cvs.imshow(res_img)
