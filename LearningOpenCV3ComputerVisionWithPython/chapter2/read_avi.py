# -*- coding: utf-8 -*-
"""
Created on Sat May  4 09:17:13 2019

@author: xjr76
"""

import cv2


videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('MyOutputVid.avi',
                              cv2.VideoWriter_fourcc('I', '4', '2', '0'),
                              fps,
                              size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()