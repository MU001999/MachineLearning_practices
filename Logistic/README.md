# Logistic
## Logistic回归的一般过程
1. 收集数据
	* 采用任意方法收集数据
1. 准备数据
	* 由于需要进行距离计算，因此要求数据类型为数值型。另外，结构化数据格式最佳。
1. 分析数据
	* 采用任意方法对数据进行分析。
1. 训练算法
	* 大部分时间将用于训练，训练的目的是为了找到最佳的分类回归系统。
1. 测试算法
	* 一旦训练步骤完成，分类将会很快。
1. 使用算法
	* 首先，我们需要输入一些数据，并将其转换成对应的结构化数值；<br>接着，基于训练好的回归系数就可以对这些数值进行简单的回归计算，判定它们属于哪个类别；<br>在这之后，我们就可以在输出的类别上做一些其他分析工作。

### 优点
计算代价不高，易于理解和实现

### 缺点
容易欠拟合，分类精度可能不高

### 适用数据类型
数值型和标称型数据