# the description of Decision Tree
1. 创建节点N
2. 如果训练集为空，在返回节点N标记为Failure
3. 如果训练集中的所有记录都属于同一个类别，则以该类别标记节点N
4. 如果候选属性为空，则返回N作为叶节点，标记为训练集中最普通的类；
5. for each 候选属性 attribute_list
6. if 候选属性是连续的then
7. 对该属性进行离散化
8. 选择候选属性attribute_list中具有最高信息增益率的属性D
9. 标记节点N为属性D
10. for each 属性D的一致值d
11. 由节点N长出一个条件为D=d的分支
12. 设s是训练集中D=d的训练样本的集合
13. if s为空
14. 加上一个树叶，标记为训练集中最普通的类
15. else加上一个有C4.5（R - {D},C，s）返回的点
