from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train/weights/best.pt")
cap = cv2.VideoCapture("origin.avi")

fps = int(cap.get(cv2.CAP_PROP_FPS))
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    results = model(frame)
    annotated = results[0].plot()
    out.write(annotated)

cap.release()
out.release()
print("推理完成 → output.mp4")