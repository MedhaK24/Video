import cv2
import os
path = 'Images'
allimages = sorted (os.listdir(path))
images = []
for eachimage in allimages: 
    newpath = path+'/'+eachimage 
    images.append(newpath)
frame=cv2.imread(images[0])
height, width, channels=frame.shape
size=(width,height)
newvideo=cv2.VideoWriter('sunrise.mp4',cv2.VideoWriter_fourcc(*'DIVX'),5,size)
for eachimage in reversed (images):
    frame=cv2.imread(eachimage)
    newvideo.write(frame)
newvideo.release()
