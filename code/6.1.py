from ultralytics import YOLO

model = YOLO(r"/home/wrt/task_6/runs/detect/train1/weights/best.pt")
model.predict(
     source=r"/home/wrt/task_6/origin.mp4",
     save=False,
     show=True,
     line_width=2,
)
