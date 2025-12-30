#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>
#include <cstdio>
#include <string>
using namespace std;
using namespace cv;


int main( ){
    VideoCapture video("/home/wrt/origin.avi");
    Mat a;
    char image[10000];
    int frame_idx=0;
    string path="/home/wrt/video_frame";
     while(true){
        video >> a;
          if (a.empty()) break;
                
            
        sprintf(image,"/home/wrt/video_frame/%06d.jpg",frame_idx++);
            imwrite(image,a);
     }
     return 0;
               
}


