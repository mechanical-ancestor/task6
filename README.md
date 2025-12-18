# task6

**1. 简介**

考核五为YOLO神经网络考核，神经网络（Neural Network）是一类受生物神经系统启发的数学模型与算法，用于从数据中自动学习映射关系或表示，常见前馈神经网络（FNN）、卷积神经网络（CNN，用于图像）、循环神经网络（RNN，用于序列）、Transformer（用于语言和序列任务）等。YOLO基于深度神经网络（主要是卷积神经网络，CNN）构建的检测器，目的是在单次前向传播中同时预测图像中的物体类别和边界框。

**2. 结构介绍**

- assets文件夹：
    - example.gif：示例gif动图
    - origin.avi：需要识别的原始视频
- code文件夹：
    - 存放你的源代码以及CMakeLists.txt文件

- README.md：任务说明文档

## 任务：yolo识别

你需要制作数据集，借助yolo训练模型，然对origin视频中的装甲板进行识别。

提示：

1.对于数据集的获取，你可以写一个截取视频帧的代码，这样的获取方式比截屏方便的多

2.对于数据集的标注，你可选择下载labelme软件对图像需识别区域进行标注，这需要你自己手动操作

3.标注好后，你需要更改数据集格式，变成yolo可训练的格式，这里你也可以写代码完成

4.训练完成后会得到一个最优模型，使用最优模型对视频进行识别即可



## 上传要求（很重要，必须看）

上传要求同考核5，并附加以下要求：

1.上传的gif大小不可超过50m，你需要对运行结果降质。

2.该md最后有个result,你只需模仿我的写法将你的运行结果gif放在该md文件里即可

## 运行结果

**example:**   * *的例子:* *

![example.gif](/assets/example.gif)

**result:**   * *结果:* *

> 使用了yolov12和yolov13训练，在视频中每秒截取了5张图像，原始图像共108张，使用[roboflow](https://app.roboflow.com/rmtext-0twfr/my-first-project-nummy/1)进行标注和图像增强，yolo中有进行二次图像增强。两次训练均采用相同的数据集和超参数
> - 标注质量有点低
> - batch == 16

- yolov13  
  ![v13.png](/assets/results_v13.png)
  - 默认置信度  
    ![v13.gif](/assets/v13.gif)
  - conf == 0.6  
    ![v13_conf.gif](/assets/v13_conf.gif)
- yolov12  
  ![v12.png](/assets/results_v12.png)
  - 默认置信度  
    ![v12.gif](/assets/v12.gif)
  - conf == 0.6  
    ![v12_conf.gif](/assets/v12_conf.gif)

>tips：v12挺有意思的，在使用attention的情况下还保证了不错的推理速度（之前用swin-T给我卡成定格动画了），后期在深入去对比一下




