#  A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots
|               | A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots |
| ------------- | -------------            |
| 作者信息 |  Alessandro Giusti1 et al. Dalle Molle Institute for Artificial Intelligence (IDSIA)  |
| 发表情况 |  IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED NOVEMBER, 2015      |
| 被引次数 | 15 until 20170208             |
| 阅读时间 | 2017年2月8日--9日              |
| 论文领域 | Visual-Based Navigation; Aerial Robotics; Machine Learning; Deep Learning        |  
| 技术难点 | 小径与周围环境像素融合较好，使用传统的基于像素差异的方法进行小径识别难以有好的效果       |
| 主要创新 | 实现了 基于DNN的小径感知技术，并提供了实验数据集以及视频进行支撑 |

## 原文摘要
通过在小路上行进的机器人的视线，我们研究了从单目图像进行森林或者山峦小径感知的问题。之前的文献专注于小径分割(trail segmentation) 以及使用诸如显著图像或者外观对比(image saliency or appearance contrast)等的低级特征。我们基于将DNN(Deep Neural Network)最为一个监督图像分类器提出了一种不同的方法。通过对完整图像的一次操作，我们的系统在与视角方向的比对下输出了小径的主要方向。基于一个大型的真实世界的数据集，定性以及定量的结果显示我们的方法优于选择的方法，同时，在对同一个图像方向分类任务的测试中我们系统的准确性可以媲美人类的准确性。初步的关于在看不见得到小径中的螺旋翼控制信息的结构被报道出来了(此文)。据我们所知，这篇文章是第一篇描述一种使用四旋翼微型飞行器(quadrotor micro aerial vehicle)感知森林小径的方法的文章。

## 总体思路
![](./img/A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots1.png)
![](./img/A Machine Learning Approach to Visual Perception of Forest Trails for Mobile Robots2.png)
