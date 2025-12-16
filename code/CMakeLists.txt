cmake_minimum_required(VERSION 3.10)
project(FrameCapture)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# # 查找 OpenCV 包
find_package(OpenCV REQUIRED)

# 包含头文件目录
include_directories(${OpenCV_INCLUDE_DIRS})

# 添加可执行文件
add_executable(frame_capture frame_cap.cpp)

# 链接 OpenCV 库
target_link_libraries(frame_capture ${OpenCV_LIBS})