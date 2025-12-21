import json, os
from PIL import Image

image_dir = "dataset/images"
label_dir = "dataset/labels"
os.makedirs(label_dir, exist_ok=True)

for f in os.listdir(image_dir):
    if not f.endswith(".json"): continue
    with open(f"{image_dir}/{f}") as jf:
        data = json.load(jf)
    img = Image.open(f"{image_dir}/{f.replace('.json','.jpg')}")
    w, h = img.size

    lines = []
    for shape in data["shapes"]:
        if shape["label"] != "armor": continue
        pts = shape["points"]
        x_min, x_max = min(p[0] for p in pts), max(p[0] for p in pts)
        y_min, y_max = min(p[1] for p in pts), max(p[1] for p in pts)
        xc, yc = (x_min+x_max)/2/w, (y_min+y_max)/2/h
        bw, bh = (x_max-x_min)/w, (y_max-y_min)/h
        lines.append(f"0 {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}")

    with open(f"{label_dir}/{f.replace('.json','.txt')}", "w") as tf:
        tf.write("\n".join(lines))

print("YOLO 格式标注已保存到 dataset/labels/")