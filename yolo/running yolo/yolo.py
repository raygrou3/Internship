from ultralytics import YOLO
import cv2
model=YOLO('../yoloWeights/yolov8n.pt')
results=model("Images/5.jpg",show=True)
cv2.waitKey(0)
