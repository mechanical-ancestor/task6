import json
import os
import cv2
images_path = "dataset/images"
labels_path = "dataset/labels"
class_map = {"armor": 0}
for json_file in os.listdir(labels_path):
    if not json_file.endswith(".json"):
        continue
    json_path = os.path.join(labels_path, json_file)
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    img_name = data["imagePath"]
    img_path = os.path.join(images_path, img_name)
    img = cv2.imread(img_path)
    if img is None:
        print(f"⚠️ 图片{img_path}不存在，跳过")
        continue
    h, w, _ = img.shape
    txt_file = json_file.replace(".json", ".txt")
    txt_path = os.path.join(labels_path, txt_file)
    with open(txt_path, "w") as f:
        for shape in data["shapes"]:
            x1, y1 = shape["points"][0]
            x2, y2 = shape["points"][1]
            cx = (x1 + x2) / (2 * w)
            cy = (y1 + y2) / (2 * h)
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h
            class_id = class_map[shape["label"]]
            f.write(f"{class_id} {cx:.6f} {cy:.6f} {bw:.6f} {bh:.6f}\n")
    os.remove(json_path)

print("✅ 标注格式转换完成！labels目录下生成YOLO格式.txt文件")
