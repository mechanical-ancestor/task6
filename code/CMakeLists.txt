cmake_minimum_required(VERSION 3.20)
project(yolo_cpp)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(main task6.cpp)

target_link_libraries(main ${OpenCV_LIBS})