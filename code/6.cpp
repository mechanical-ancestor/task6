#include<opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;
int main ()
{
    cv::Mat frame1;
cv::VideoCapture cap("/home/wang-zhichou/下载/1.avi");//讀取視頻文件
    char image[1500];
    int i=0;
while(cap.read(frame1)){
cap >> frame1;
sprintf(image, "%s%d%s", "/home/wang-zhichou/local_repositories/task6/data", i++, ".jpg"); 
cv::imwrite(image, frame1);//截取視頻幀並保存為圖片
}
  return 0;
}
/*終端命令
訓練模型：yolo task=detect 
mode=train     
model=yolov8n.pt     
data=/home/wang-zhichou/local_repositories/task6/labelme_jsons1/YOLODataset/dataset.yaml    
 epochs=100     imgsz=640
使用模型：yolo predict model=/home/wang-zhichou/ultralytics/runs/detect/train5/weights/best.pt source='/home/wang-zhichou/下载/1.avi' save=true show=false
*/