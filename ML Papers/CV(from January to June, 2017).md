#  Scene Graph Generation by Iterative Message Passing
|               | Scene Graph Generation by Iterative Message Passing |
| ------------- | -------------            |
| 作者信息  | 李飞飞 Li Fei-Fei             |
| 发表情况 | 2017年1月10日于arxiv           |
| 被引次数 | 0 until 20170205              |
| 阅读时间 | 2017年2月4日--6日              |
| 论文领域 | Scene Graph Generation        |
| 主要创新 | 在理解视觉场景时，不再像之前只是理解单独的物体，而是将物体之间的关系(提供了丰富的关于这个场景的语义信息(semantic information).)进行重点考虑 |
| 大体思路 |  使用场景图明确地对物体及其关系进行建模。提出了一种全新的端到端模型，其可以从输入图像中生成这种结构化的场景表征(scene representation)。该模型可以使用标准RNN解决场景图推理问题(scene graph inference problem)以及通过信息传递(message passing)学习迭代式地提升其预测能力。同时在其中使用到的联合推理模型可以利用语境线索(contextual cues)来更好地预测物体及其关系。 |
| 个人思考 |                  fasf         |



table {
    width: 100%; /*表格宽度*/
    max-width: 65em; /*表格最大宽度，避免表格过宽*/
    border: 1px solid #dedede; /*表格外边框设置*/
    margin: 15px auto; /*外边距*/
    border-collapse: collapse; /*使用单一线条的边框*/
    empty-cells: show; /*单元格无内容依旧绘制边框*/
}

table th,
table td {
  height: 35px; /*统一每一行的默认高度*/
  border: 1px solid #dedede; /*内部边框样式*/
  padding: 0 10px; /*内边距*/
}
