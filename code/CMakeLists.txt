cmake_minimum_required(VERSION 3.10)
project(video_frame_extractor)

set(CMAKE_CXX_STANDARD 14)

# 查找 OpenCV 库
find_package(OpenCV REQUIRED)

# 添加可执行文件
add_executable(${PROJECT_NAME} src/main.cpp)

# 链接 OpenCV 库
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

# 输出目录设置
set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin)
