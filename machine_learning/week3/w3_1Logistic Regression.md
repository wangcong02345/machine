# Week3_1Logistic Regression

### 第 1 题
Suppose that you have trained a logistic regression classifier, and it outputs on a new example x a prediction $h_\theta(x)$ = 0.4. This means (check all that apply):

* Our estimate for $P(y=0|x;\theta)$ is 0.4.
* Our estimate for $P(y=1|x;\theta)$ is 0.6.
* Our estimate for $P(y=0|x;\theta)$ is 0.6.
* Our estimate for $P(y=1|x;\theta)$ is 0.4.  
<font color=red> ** &nbsp;&nbsp;&nbsp;&nbsp;答案: 3 4 **</font>  
<font color=red> **&nbsp;&nbsp;&nbsp;&nbsp;解析: $h_\theta(x)$ will give us the probability that our output is 1.  0.4是y=1时的概率 **</font>  


---
### 第 2 题
Suppose you have the following training set, and fit a logistic regression classifier $h_\theta(x) = g(\theta_0 + \theta_1x_1 + \theta_2 x_2)$
Which of the following are true? Check all that apply.

* Adding polynomial features (e.g., instead using $h_\theta(x) = g(\theta_0 + \theta_1x_1 + \theta_2 x_2 + \theta_3 x_1^2 + \theta_4 x_1 x_2 + \theta_5 x_2^2)$ ) could increase how well we can fit the training data.
* At the optimal value of θ (e.g., found by fminunc), we will have J(θ)≥0.
* Adding polynomial features (e.g., instead using $h_\theta(x) = g(\theta_0 + \theta_1x_1 + \theta_2 x_2 + \theta_3 x_1^2 + \theta_4 x_1 x_2 + \theta_5 x_2^2)$ ) would increase J(θ) because we are now summing over more terms.
* If we train gradient descent for enough iterations, for some examples x(i) in the training set it is possible to obtain $h_\theta(x^{(i)}) > 1$.  
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 2 </font> **  
** <font color=red>  当有一个feature时是一条直线,当有两个feature时一条曲线,有更多的feature时是一条弯七弯八的曲线  </font> **   
** <font color=red>  当feature越来越多时,曲线越来越拟合,即损失函数越来越小 </font> **  
** <font color=red>  * 选项1: 当增加feature时,拟合的更好. 正确   </font> **  
** <font color=red>  * 选项2: 找到最佳的$\theta$,$J(\theta)$有可能为0,但一般情况下会大于0. 正确   </font> **  
** <font color=red>  * 选项3: 跟1正好相反. 不正确  </font> **  
** <font color=red>  * 选项4: $0<h_\theta(x^{(i)})<1$ 的0到1之间不可能大于1. 不正确  </font> **  

--- 
### 第 3 题

第 3 个问题
For logistic regression, the gradient is given by $\frac{\partial}{\partial \theta_j} J(\theta) =\frac{1}{m}\sum_{i=1}^m{ (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}}$. Which of these is a correct gradient descent update for logistic regression with a learning rate of α? Check all that apply. 

 * $\theta := \theta - \alpha \frac{1}{m} \sum_{i=1}^m{ \left(\theta^T x - y^{(i)}\right) x^{(i)}}$
 * $\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m{ \left(\frac{1}{1 + e^{-\theta^T x^{(i)}}} - y^{(i)}\right) x_j^{(i)}}$  (simultaneously update for all $j$).
 * $\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m{ (h_\theta(x^{(i)}) - y^{(i)}) x^{(i)}}$(simultaneously update for all $j$).
 * $\theta_j := \theta_j - \alpha \frac{1}{m} \sum_{i=1}^m{ (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}}$ (simultaneously update for all $j$).
 
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 4  </font> **  
** <font color=red>  * 选项1: $\theta^T x$,是线性回归的. 不正确   </font> **  
** <font color=red>  * 选项2: 正确   </font> **  
** <font color=red>  * 选项3: 与4的区别是$x^{(i)}$ 与 $x_j^{(i)}$,不明白的话需要看一下推导过程. 不正确  </font> **  
** <font color=red>  * 选项4: 正确  </font> ** 

---

### 第 4 题
Which of the following statements are true? Check all that apply.

* For logistic regression, sometimes gradient descent will converge to a local minimum (and fail to find the global minimum). This is the reason we prefer more advanced optimization algorithms such as fminunc (conjugate gradient/BFGS/L-BFGS/etc).
* The sigmoid function $g(z) = \frac{1}{1 + e^{-z}}$ is never greater than one (>1).
* The cost function J(θ) for logistic regression trained with m≥1 examples is always greater than or equal to zero.
* Linear regression always works well for classification if you classify by using a threshold on the prediction made by linear regression.  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 3  </font> **  
** <font color=red>  * 选项1: 梯度下降法是能找到全局最小值的,因为损失函数是一个凸函数.用更高级的算法的目的是"no need to pick $\alpha$",同时更快速的找到全局最小值  </font> **  
** <font color=red>  * 选项2: sigmoid函数的取值范围是(0,1). 正确   </font> **  
** <font color=red>  * 选项3: costFunction 大于等于0. 正确  </font> **  
** <font color=red>  * 选项4: 分类问题,要么0, 要么1, 没有什么threshold一说  </font> ** 

---
## 第 5 题
第 5 个问题
Suppose you train a logistic classifier $h_\theta(x) = g(\theta_0 + \theta_1x_1 + \theta_2 x_2)$. Suppose θ0=6,θ1=−1,θ2=0. Which of the following figures represents the decision boundary found by your classifier?

** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 刷了几次没有选项,只有题干,随便蒙了一个竟然对了  </font> **  

