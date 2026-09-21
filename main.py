
from ultralytics import YOLO

model = YOLO("yolov8n.yaml")
# model = YOLO("yolov8n.pt")

model.train(data="data.yaml", epochs=80)


