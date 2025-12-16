#include <iostream>
#include <string>
#include <vector>
#include <filesystem>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;
namespace fs = std::filesystem;

int main() {
    string videoPath = "../assets/origin.avi";
    // 
    VideoCapture cap(videoPath);    
    if (!cap.isOpened()) {
        cerr << "错误：无法打开视频文件！" << endl;
        return -1;
    }
    
    // 获取视频信息
    double fps = cap.get(cv::CAP_PROP_FPS);
    cout << "视频信息：" << endl;
    cout << "帧率: " << fps << " fps" << endl;
    
    // 创建输出目录
    string outputDir = "../dataset/images"; 
    if (!fs::exists(outputDir)) {
        if (!fs::create_directories(outputDir)) { 
            cerr << "错误：无法创建输出目录！" << endl;
            return -1;
        }
    }
    
    cout << "\n开始提取帧..." << endl;
    
    Mat frame;
    int frameCount = 0;
    int savedCount = 0;
    int fileIndex = 1;
    
    while (true) {
        cap >> frame;
        if (frame.empty()) {
            break;  
        }

        frameCount++;
        
        if (frameCount % 8 == 0) {
            string filename = outputDir + "/frame_" + to_string(fileIndex++) + ".jpg";
            
            // 保存为JPEG
            vector<int> compression_params;
            compression_params.push_back(cv::IMWRITE_JPEG_QUALITY);
            compression_params.push_back(95);  
            
            if (imwrite(filename, frame, compression_params)) {
                savedCount++;
                
                // 显示进度（去掉百分比计算）
                if (savedCount % 10 == 0 || savedCount == 1) {
                    cout << "已保存 " << savedCount << " 帧" << endl;
                }
            } 
            else {
                cerr << "警告：无法保存帧 " << frameCount << endl;
            }
        }
        
        // 显示当前帧
        imshow("正在提取... 按ESC退出", frame);
        if (waitKey(1) == 27) {  // ESC键退出
            cout << "\n用户中断提取过程" << endl;
            break;
        }
    }
    
    cap.release();
    destroyAllWindows();
    
    cout << "\n=== 提取完成 ===" << endl;
    cout << "总共读取: " << frameCount << " 帧" << endl;
    cout << "成功保存: " << savedCount << " 帧" << endl;
    
    return 0;
}