cmake_minimum_required(VERSION 3.20)

project(project_sixth)

set(OpenCV_DIR "${CMAKE_CURRENT_SOURCE_DIR}/usr/local/lib/cmake/opencv4")

find_package(OpenCV REQUIRED)

include_directories(${OpenCV_INCLUDE_DIRS})

add_executable(capture src/capture.cpp)

target_link_libraries(capture ${OpenCV_LIBS})