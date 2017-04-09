# the description of kNN :

1.	依公式计算 Item 与 D1、D2 … …、Dj 之相似度。得到Sim(Item, D1)、Sim(Item, D2)… …、Sim(Item, Dj)。
1.	将Sim(Item, D1)、Sim(Item, D2)… …、Sim(Item, Dj)排序，若是超过相似度阈值t则放入邻居案例集合NN。
1.	自邻居案例集合NN中取出前k名，依多数决，得到Item可能类别。

### 关于一维至N维的相似度计算问题推演

![](http://www.jusot.com/wp-content/uploads/2017/03/16300000349743126968424616674_s-300x125.jpg)
