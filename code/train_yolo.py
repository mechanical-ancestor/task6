from ultralytics import YOLO
model = YOLO("yolov8n.pt")
results = model.train(
    data="dataset.yaml",  
    epochs=200,            
    imgsz=640,           
    batch=8,             
    device="cpu"          
)
metrics = model.val()
print(f"✅ 模型训练完成！验证集mAP：{metrics.box.map:.4f}")

