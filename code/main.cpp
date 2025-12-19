//提取每一帧并保存图片

#include<opencv2/opencv.hpp>
using namespace cv;

int main() {
    VideoCapture cap("/home/wanqing/my_code/task_6/vedio_frame_extractor/txt_img/origin.avi");
    Mat frame;
    char image[2000];
    int i = 0;
    
    while(cap.read(frame)) {
        sprintf(image, "/home/wanqing/my_code/task_6/vedio_frame_extractor/txt_img/frame_%d.jpg", i++);
        imwrite(image, frame);
    }
    
    return 0;
}
