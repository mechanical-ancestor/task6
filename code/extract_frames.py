import subprocess
import os
video_path = "/home/aurora/task6/assets/origin.avi"
save_path = "dataset/images"
frame_interval = 5
os.makedirs(save_path, exist_ok=True)
def extract_frames():
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"fps=1/{frame_interval}",
        "-q:v", "2", 
        f"{save_path}/frame_%04d.jpg"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        frame_files = [f for f in os.listdir(save_path) if f.startswith("frame_")]
        print(f"✅ 截帧成功！共提取{len(frame_files)}帧，保存在{save_path}")
    else:
        print(f"❌ 截帧失败！错误信息：{result.stderr}")

if __name__ == "__main__":
    extract_frames()
