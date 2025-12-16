from ultralytics import YOLO
import torch

# if torch.cuda.is_available():
#     device = '0'
#     print(f"✅ 使用GPU: {torch.cuda.get_device_name(0)}")
# else:
#     device = 'cpu'
#     print("⚠️  使用CPU (训练会较慢)")

# 加载模型
model = YOLO('yolov8n.pt') 

# 开始训练
model.train(
    data='dataset/data.yaml',
    epochs=100,              # 训练100轮
    imgsz=640,
    batch=8,                 # 批次大小
    device='cpu',
    name='armor_final_v1',
    save=True,
    save_period=10,          # 每10轮保存一次检查点
    plots=True,              # 生成训练图表
    verbose=True
)

print("\n✅ 训练完成！")
print("📁 模型保存在: runs/detect/armor_final_v1/")
print("🏆 最佳模型: runs/detect/armor_final_v1/weights/best.pt")