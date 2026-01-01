from ultralytics import YOLO
import cv2
model = YOLO("runs/detect/train4/weights/best.pt")
video_path = "../assets/origin.avi"
output_path = "../assets/result_video.avi"
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = model(frame, conf=0.05)
    frame_with_box = results[0].plot()
    out.write(frame_with_box)
cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ 带检测框的视频生成完成！")

