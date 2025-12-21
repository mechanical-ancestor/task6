import cv2
import os

os.makedirs("dataset/images", exist_ok=True)
cap = cv2.VideoCapture("origin.avi")
frame_id = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # 每 10 帧保存 1 帧
    if frame_id % 10 == 0:
        cv2.imwrite(f"dataset/images/{frame_id:05d}.jpg", frame)
    frame_id += 1

cap.release()
print(f"保存了约 {frame_id//10} 张图片到 dataset/images/")