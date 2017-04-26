#  Learning Transferable Policies for Monocular Reactive MAV Control
|               | Learning Transferable Policies for Monocular Reactive MAV Control |
| ------------- | -------------            |
| 作者信息 | Shreyansh Daftry, J. Andrew Bagnell, Martial Hebert  |
| 发表情况 | Submitted on 1 Aug 2016 on arXiv, ISER 2016      |
| 被引次数 | 2 until 20170208             |
| 阅读时间 | 2017年2月9日              |
| 论文领域 | Transfer Learning, Domain Adaptation, Reactive Control, Autonomous Monocular Navigation, MAV |  
| 技术难点 | 如何将源域中的训练能力来解决未知域(目标域)中的问题 |
| 主要创新 | DAN(Deep Adaptation Network)在无人机迁移学习中的实现 |

## 原文摘要
迁移从先前任务获得的知识到下一个任务的能力是人类学习最为重要的机制。尽管如此，能够在一个部分相似的环境中适应自主行为仍然是机器人研究中一件棘手的事情。在这篇文章中，我们朝着这个方向前进了一小步：提出了一个学习可迁移的行为的策略的通用框架。我们的目标是通过使用源域(source domain)中的训练数据来解决与源域不同但是相关的目标域中的学习问题。我们通过使用monocular reactive control的自主微型飞行器(MAV--Micro Aerial Vehicles)以及通过大量的实地的户外复杂环境的飞行试验来呈现我们提出方法的成果。

**注：** 此文章更加注重应用性而不是理论性，因此大量的篇幅是对于具体实践的说明以及效果的展示。

## 总体思路 
首先在源域(D={xi,yi})中考虑降低交叉域的差异进行模型的学习,然后将其应用于Dt={xj},来进行飞行器螺旋桨左右速度的调整。

此篇文章也可以说是将DAN(Deep Adaptation Network)在无人机迁移学习中的实现，DAN是deep learning的一种适应性拓展，在这篇文章中，主要目的是降低目标域与源域的模型化差异度。

![](./img/Learning Transferable Policies for Monocular Reactive MAV Control1.png)

## 试验设计
该方法从ARDrone飞行器到ArduCopter飞行器的迁移，从夏天到冬天的迁移，从苏黎世大学到卡耐基梅隆大学进行的迁移，说明了在一定程度上，基于DAN的方法起到了比较好的效果。

![](./img/Learning Transferable Policies for Monocular Reactive MAV Control2.png)
