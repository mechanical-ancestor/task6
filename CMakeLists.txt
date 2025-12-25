cmake_minimum_required(VERSION 3.10)
project(YOLO_Armor_Detection)
find_package(Python3 REQUIRED COMPONENTS Interpreter)
add_custom_target(train ALL COMMAND ${Python3_EXECUTABLE} train_yolo.py WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
add_custom_target(infer ALL COMMAND ${Python3_EXECUTABLE} infer_video.py WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
install(PROGRAMS train_yolo.py infer_video.py labelme2yolo.py DESTINATION bin)

