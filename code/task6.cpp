#include<opencv2/opencv.hpp>
#include<iostream>

using namespace std;
using namespace cv;

int main(){
   VideoCapture result;
   result.open("/home/gan/yolov11_2/results/exp/origin.avi");
   while(true){
    Mat frame;
    result>>frame;
    if(frame.empty()){
        cout<<"视频播放完毕！"<<endl;
        break;
    }
    imshow("result",frame);
    waitKey(1000/result.get(CAP_PROP_FPS));
   }
   result.release();
   destroyAllWindows();
}