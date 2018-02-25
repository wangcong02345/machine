# Week10_1Large Scale Machine Learning

### 第 1 题
Suppose you are training a logistic regression classifier using stochastic gradient descent.  
You find that the cost (say, $cost(\theta,(x^{(i)}, y^{(i)}))$), averaged over the last 500 examples),  
plotted as a function of the number of iterations, is slowly increasing over time.  
Which of the following changes are likely to help?  

* Try averaging the cost over a smaller number of examples (say 250 examples instead of 500) in the plot.  
* This is not possible with stochastic gradient descent, as it is guaranteed to converge to the optimal parameters $\theta$.  
* Try halving (decreasing) the learning rate $\alpha$, and see if that causes the cost to now consistently go down;   
   and if not, keep halving it until it does.  
* Use fewer examples from your training set.

<font color=red> ** &nbsp;&nbsp;&nbsp;&nbsp;答案: 3  **</font>  
<font color=red> **&nbsp;&nbsp;&nbsp;&nbsp;解析: 代价函数不降反升, 将$\alpha$ 的值减小一半,试一下 **</font>    

---
### 第 2 题
Which of the following statements about stochastic gradient descent are true? Check all that apply.  

* You can use the method of numerical gradient checking to verify that your stochastic gradient descent implementation is bug-free.  
  (One step of stochastic gradient descent computes the partial derivative $\frac{\partial}{\partial \theta_j} cost(\theta, (x^{(i)}, y^{(i)}))$.)
* Before running stochastic gradient descent, you should randomly shuffle (reorder) the training set.   
* Suppose you are using stochastic gradient descent to train a linear regression classifier.   
  The cost function $J(\theta) = \frac{1}{2m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)})^2$ is guaranteed to decrease after every iteration of the stochastic gradient descent algorithm.
* In order to make sure stochastic gradient descent is converging, we typically compute $J_{\rm train}(\theta)$ after each iteration (and plot it) in order to make sure that the cost function is generally decreasing.   
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 2 </font> **  
** <font color=red>  选项1:  </font> **  
** <font color=red>  选项2: 用随机梯度下降法时,首先对训练集随机'洗牌'.  正确  </font> **  
** <font color=red>  选项3: 用随机梯度下降法训练线性回归模型. costFunction不一定每次都减小,而是曲折减小,逐渐减小到全局最小值.  </font> **  
** <font color=red>  选项4: 每次迭代后是计算单一的训练实例的代价函数$cost\left(\theta, (x^{(i)}, y^{(i)})\right)=\frac{1}{2}\left(h_\theta(x^{(i)} - y^{(i)} ) \right)^2$,而不是$J_{\rm train}(\theta)$ </font> **  

--- 
### 第 3 题
Which of the following statements about online learning are true? Check all that apply.  

 * Online learning algorithms are usually best suited to problems were we have a continuous/non-stop stream of data that we want to learn from.  
 * Online learning algorithms are most appropriate when we have a fixed training set of size m that we want to train on.  
 * When using online learning, you must save every new training example you get, as you will need to reuse past examples to re-train the model even after you get new training examples in the future. 
 * One of the advantages of online learning is that if the function we're modeling changes over time (such as if we are modeling the probability of users clicking on different URLs, and user tastes/preferences are changing over time), the online learning algorithm will automatically adapt to these changes.   
 
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 4 </font> **  
** <font color=red>  选项1: Online learning algorithms 适合于不间断的数据stream的情况下.  正确.</font> **  
** <font color=red>  选项2: Online learning algorithms 适合于不间断的数据stream的情况下,而不是fixed.  不正确.</font> **  
** <font color=red>  选项3: Online learning algorithms 不需要数据重复利用,数据是一次性.  不正确.</font> **  
** <font color=red>  选项3: Online learning algorithms 的模型会实时变化，因为数据实时变化，那么算法也要实时自动变化.  正确.</font> **  

---

### 第 4 题
Assuming that you have a very large training set, which of the following algorithms do you think can be parallelized using map-reduce and splitting the training set across different machines? Check all that apply.

* Logistic regression trained using stochastic gradient descent. 
* Linear regression trained using stochastic gradient descent. 
* Logistic regression trained using batch gradient descent. 
* Computing the average of all the features in your training set $\mu = \frac{1}{m} \sum_{i=1}^m x^{(i)}$ (say in order to perform mean normalization).   
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 3 4  </font> **  
** <font color=red>  如果你有很大的数据量,下面哪一个算法可以用来做并行的map-reduce,然后把数据分到不同的计算机上去做并行计算. </font> **  
** <font color=red>  选项1: 随机梯度下降法一次只用一个样本,没法做并行. 不正确 </font> **  
** <font color=red>  选项2: 同上1.  不正确 </font> **  
** <font color=red>  选项3: 批量的梯度下降是可以的,因为可以把数据分为N个小batch,然后分别计算. 正确 </font> **  
** <font color=red>  选项4: 这个跟批量是同一个道理, 都可以把数据分为N个小数据包,然后分别计算. 正确 </font> **  

---
## 第 5 题
Which of the following statements about map-reduce are true? Check all that apply.  

* Because of network latency and other overhead associated with map-reduce, if we run map-reduce using N computers, we might get less than an N-fold speedup compared to using 1 computer.  
* If you have only 1 computer with 1 computing core, then map-reduce is unlikely to help.
* When using map-reduce with gradient descent, we usually use a single machine that accumulates the gradients from each of the map-reduce machines, in order to compute the parameter update for that iteration.
* Linear regression and logistic regression can be parallelized using map-reduce, but not neural network training.  

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 2 3  </font> **  
** <font color=red>  选项1: 因为有网络延时和其它情况,所以用N台计算机做map-reduce所达到的效果,不会有N倍的提升,一般会小于N倍.  正确 </font> ** 
** <font color=red>  选项2: 如果你只有一台计算机一个核,那么用map-reduce是没有用的.  正确 </font> **  
** <font color=red>  选项3: 做map-reduce时用一台计算机做汇总, 汇总其它计算机产生的gradients数据.  正确 </font> **  
** <font color=red>  选项4: 线性回归 logistic回归 和 神经网络都可以用map-reduce.  不正确 </font> **  
