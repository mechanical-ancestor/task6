#include <iostream>
#include <opencv2/opencv.hpp>
#include <string>
#include <stdexcept>
#include <filesystem>
 
// 函数声明
void videoToImages(const std::string& videoPath, const std::string& outputDir, int frameInterval);
 
int main() {
    std::string videoPath;
    std::string outputDir;
    int frameInterval;
 
    // 获取用户输入
    std::cout << "请输入视频文件路径: ";
    std::cin >> videoPath;
    std::cout << "请输入输出图片文件夹路径: ";
    std::cin >> outputDir;
    std::cout << "请输入帧提取间隔（例如每秒1帧输入25）: ";
    std::cin >> frameInterval;
 
    try {
        // 调用视频转图片函数
        videoToImages(videoPath, outputDir, frameInterval);
        std::cout << "视频帧提取完成！" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "错误: " << e.what() << std::endl;
    }
 
    return 0;
}
 
// 视频转图片函数
void videoToImages(const std::string& videoPath, const std::string& outputDir, int frameInterval) {
    // 打开视频文件
    cv::VideoCapture videoCapture(videoPath);
    if (!videoCapture.isOpened()) {
        throw std::runtime_error("无法打开视频文件: " + videoPath);
    }
 
    // 获取视频帧率
    double fps = videoCapture.get(cv::CAP_PROP_FPS);
    if (fps <= 0) {
        throw std::runtime_error("无法获取视频帧率。");
    }
 
    // 计算帧间隔
    int frameStep = static_cast<int>(fps / frameInterval);
    if (frameStep <= 0) {
        frameStep = 1;
    }
 
    // 创建输出文件夹
    if (!std::filesystem::exists(outputDir)) {
        if (!std::filesystem::create_directories(outputDir)) {
            throw std::runtime_error("无法创建输出文件夹: " + outputDir);
        }
    }
 
    // 逐帧读取视频
    cv::Mat frame;
    int frameCount = 0;
    int savedFrameCount = 0;
 
    while (videoCapture.read(frame)) {
        if (frameCount % frameStep == 0) {
            // 生成图片文件名
            std::string imagePath = outputDir + "/frame_" + std::to_string(savedFrameCount) + ".jpg";
 
            // 保存帧为图片
            if (!cv::imwrite(imagePath, frame)) {
                throw std::runtime_error("无法保存图片: " + imagePath);
            }
            std::cout << "保存图片: " << imagePath << std::endl;
            savedFrameCount++;
        }
        frameCount++;
    }
 
    // 释放视频资源
    videoCapture.release();
}