import cv2 as cv
from ultralytics import YOLO

model = YOLO("/home/gan/ultralytics/runs/detect/train14_MA/weights/best.pt")

results = model.predict(
    source = "/home/gan/Photo_Set_1/25.jpg",
    conf=0.30,
    iou=0.25,
    save=True,
    show=True,
    project="results",
    name="test_1",
    device="cpu"
)
