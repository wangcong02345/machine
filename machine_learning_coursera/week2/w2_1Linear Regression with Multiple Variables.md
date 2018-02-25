# Week 2 | 1Linear Regression with Multiple Variables

### 第 1 题
Suppose m=4 students have taken some class, and the class had a midterm exam and a final exam. You have collected a dataset of their scores on the two exams, which is as follows:

| midterm exam | (midterm exam)^2 | final exam |
|--------------|------------------|------------|
| 89 | 7921 | 96 |
|72|5184|74|
|94|8836|87|
|69|4761|78|

You'd like to use polynomial regression to predict a student's final exam score from their midterm exam score. Concretely, suppose you want to fit a model of the form $h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2$, where x1 is the midterm score and x2 is (midterm score)2. Further, you plan to use both feature scaling (dividing by the "max-min", or range, of a feature) and mean normalization. 
What is the normalized feature $x_2^{(4)}$? (Hint: midterm = 89, final = 96 is training example 1.) Please enter your answer in the text box below. If applicable, please provide at least two digits after the decimal place.  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 4  
&nbsp;&nbsp;&nbsp;&nbsp;解析: 将数据代入公式就可以求得结果,公式: $x_i := \dfrac{x_i - \mu_i}{s_i}$  
其中: $\mu_i$ 是这一列数据的平均数 $(7921+5184+8836+4761)/4=6675.5$   
$s_i$ is the range of values (max - min), $(8836-4761)=4075$  
所以最终的结果是 $(4761-6675.5)/4075=-0.46981595092024539877300613496933 \approx -0.47$ </font> **


---
### 第 2 题
You run gradient descent for 15 iterations with α=0.3 and compute J(θ) after each iteration. You find that the value of J(θ) decreases slowly and is still decreasing after 15 iterations. Based on this, which of the following conclusions seems most plausible?  

* $\alpha = 0.3$  is an effective choice of learning rate.   
* Rather than use the current value of $\alpha$, it'd be more promising to try a smaller value of $\alpha$ (say $\alpha = 0.1$).  
*  Rather than use the current value of $\alpha$, it'd be more promising to try a larger value of $\alpha$ (say $\alpha = 1.0$)   
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 2  
&nbsp;&nbsp;&nbsp;&nbsp;解析: 用步长0.3发现每次迭代之后$J(\theta)$的值越来越大了,误差越来越大了.   说明越过了局部最小值,这时候就需要更小的步长去迭代 </font> ** 
   
--- 

### 第 3 题

Suppose you have m=14 training examples with n=3 features (excluding the additional all-ones feature for the intercept term, which you should add). The normal equation is $\theta = (X^TX)^{-1}X^Ty$. For the given values of m and n, what are the dimensions of θ, X, and y in this equation?  

 * X is 14×3, y is 14×1, θ is 3×3  
 * X is 14×4, y is 14×1, θ is 4×1  
 * X is 14×3, y is 14×1, θ is 3×1  
 * X is 14×4, y is 14×4, θ is 4×4  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 第2个   X is 14×4, y is 14×1, θ is 4×1  
&nbsp;&nbsp;&nbsp;&nbsp;解析: 有m=14个样本,n=3个特征,所以X是14行4列,别忘了还有一个恒为1的列  
$h_\theta=\theta_0+\theta_1 x_1+\theta_2 x_2+\theta_3 x_3$ </font> **  

---

### 第 4 题
Suppose you have a dataset with m=1000000 examples and n=200000 features for each example. You want to use multivariate linear regression to fit the parameters θ to our data. Should you prefer gradient descent or the normal equation?  

 * Gradient descent, since $(X^TX)^{-1}$ will be very slow to compute in the normal equation.
 * The normal equation, since it provides an efficient way to directly find the solution.   
 * Gradient descent, since it will always converge to the optimal θ.     
 * The normal equation, since gradient descent might be unable to find the optimal θ.  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 1  
&nbsp;&nbsp;&nbsp;&nbsp;解析: 在很大的样本及很多特征的情况下,用正规方程法去计算$(X^TX)^{-1}$的值,其时间复杂度为$O(n^3)$,   通常在n<10000时可以用正规方程法,但题目中的n=200000远远大于10000,此时用正规方程法去做时,效率会很低;  但是梯度下降法在特征数量n很大时也能较好的适用$</font> **  

---

## 第 5 题
Which of the following are reasons for using feature scaling?

* It is necessary to prevent gradient descent from getting stuck in local optima.
* It speeds up gradient descent by making each iteration of gradient descent less expensive to compute.
* It speeds up gradient descent by making it require fewer iterations to get to a good solution.
* It prevents the matrix X<sup>T</sup>X (used in the normal equation) from being non-invertable (singular/degenerate).  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 3  
&nbsp;&nbsp;&nbsp;&nbsp;解析:  
第1个选项: 归一化并不能阻止梯度下降局部最优,只是让迭代次数多而己.  
第2个选项: 归一化可以使得收敛速度加快,但选项的原因不对,数值的大小改变与计算速度无关   
第3个选项: 多维特征时,需要保证这些特征都具有相近的尺度,将所有特征的尺度都尽量缩放到-1 到 1 之间时, 等高线更接近于一个圆,而不是一个很扁的椭圆.  
当等高线接近于圆形时,可以使得迭代次数的减少，能够加快局部最小值的得出  
第4个选项: 归一化只是改变了数值大小,并不能使得矩阵不可逆  
 </font> **   

