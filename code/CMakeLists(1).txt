
cmake_minimum_required(VERSION 3.10)
project(task_6)
find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})
add_executable(task_6 6.1.cpp)
target_link_libraries(task_6 ${OpenCV_LIBS})
