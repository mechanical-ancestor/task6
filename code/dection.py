import cv2
from ultralytics import YOLO

model = YOLO("runs/detect/armor_final_v1/weights/best.pt")
video_path = "assets/origin.avi"
output_path = "assets/result.mp4"

# 视频捕获及信息
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建视频写入对象
fourcc = cv2.VideoWriter_fourcc(*'mp4v') # 编码格式
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

print("💹开始处理图像...")
frame_count = 0

while cap.isOpened() :
    ret, frame = cap.read()
    if not ret:
        break
    
    result = model(frame)               # yolo检测
    annotated_frame = result[0].plot() # 自动画框和标签
    
    out.write(annotated_frame)          
    cv2.imshow("Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"视频处理完成！结果保存到：{output_path}")