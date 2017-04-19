# The description of kNN :

1.对一个输入的新数据与已知的n个数据进行比较。

2.分别对它们进行相似度的计算,且超过相似阀值t则放入邻居案例集合NN。

3.自NN中取相似度最高的k个已知数据。

4.以k个数据中出现最多的数据的类型作为未知数据的类别。

### 关于一维至N维的相似度计算问题推演

![](http://www.jusot.com/wp-content/uploads/2017/03/16300000349743126968424616674_s-300x125.jpg)

### The Demo

1. 构建如下图所示的数据集
1. `python kNN.py --train --dataSet dataSet_path --dim num_dim` 执行训练，生成dataSet_proposed.csv
1. `python kNN.py --predict --proposed proposed_path --data data_path` 预测数据类别
