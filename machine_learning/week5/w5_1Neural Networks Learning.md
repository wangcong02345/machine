# Week5_1Neural Networks Learning
[TOC]
### 第 1 题
You are training a three layer neural network and would like to use backpropagation to compute the gradient of the cost function.   
In the backpropagation algorithm, one of the steps is to update  
$\Delta^{(2)}_{ij} := \Delta^{(2)}_{ij} +  \delta^{(3)}_i * (a^{(2)})_j$   
for every i,j. Which of the following is a correct vectorization of this step?  

* $\Delta^{(2)} := \Delta^{(2)} +  (a^{(2)})^T * \delta^{(3)}$
* $\Delta^{(2)} := \Delta^{(2)} + (a^{(3)})^T * \delta^{(2)}$
* $\Delta^{(2)} := \Delta^{(2)} +  \delta^{(3)} * (a^{(2)})^T$
* $\Delta^{(2)} := \Delta^{(2)} +  \delta^{(3)} * (a^{(3)})^T$

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 3 </font> **  
** <font color=red>      </font> **  

---
### 第 2 题
Suppose $\tt{Theta1}$ is a 5x3 matrix, and $\tt{Theta2}$ is a 4x6 matrix. You set $\tt{thetaVec = [Theta1(:) ; Theta2(:)]}$ . Which of the following correctly recovers $\tt{Theta2}$?

* $\tt{reshape(thetaVec(16:39), 4, 6)}$
* $\tt{reshape(thetaVec(15:38), 4, 6)}$
* $\tt{reshape(thetaVec(16:24), 4, 6)}$
* $\tt{reshape(thetaVec(15:39), 4, 6)}$
* $\tt{reshape(thetaVec(16:39), 6, 4)}$   
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 </font> **  
octave:1> A=[1 2 3 4 5; 6 7 8 9 10; 11 12 13 14 15]  
 $$A=\begin{bmatrix}    
    1 & 2 & 3  &4 & 5 \\
    6 & 7 & 8 & 9 & 10 \\
   11 & 12 & 13 & 14 & 15 \\  \end{bmatrix}$$    
octave:2> B=[16 17 18; 19 20 21]   
 $$B=\begin{bmatrix}        
    16 & 17 & 18 \\
    19 & 20 & 21  \end{bmatrix}$$
octave:3> V=[A(:);B(:)]  
octave:4> reshape(V(15:20),3, 2)  
$$ans = \begin{bmatrix}        
    15 & 17 \\
    16 & 20 \\
    19 & 18   \end{bmatrix}$$
octave:5> reshape(V(16:21),3, 2)  
$$ans = \begin{bmatrix}        
    16 & 20 \\
    19 & 18 \\
    17 & 21   \end{bmatrix}$$
octave:6> reshape(V(16:21),2, 3)
$$ans = \begin{bmatrix}        
    16 & 17 & 18 \\    
    19 & 20 & 21   \end{bmatrix}$$
** <font color=red> $\tt{Theta2}$ 是一个4x6的矩阵,则resharp最后的行列也是4x6 </font> **   
** <font color=red> thetaVec中$\tt{Theta2}$的开始是$\tt{Theta1}$的结束+1,即5x3+1=16 </font> **  
** <font color=red> thetaVec中$\tt{Theta2}$的结束是整个thetaVec的结束=5x3+4x6=39 </font> **  
** <font color=red>  所以最终的结果是: $\tt{reshape(thetaVec(16:39), 4, 6)}$ </font> **   
** <font color=red>  9-4 Implementation Note_Unrolling Parameters </font> ** 

--- 
### 第 3 题
Let $J(\theta) = 2 \theta^3 + 2$. Let θ=1, and $\epsilon = 0.01$. Use the formula $\frac{J(\theta + \epsilon) - J(\theta - \epsilon)}{2\epsilon}$ to numerically compute an approximation to the derivative at $\theta=1$. What value do you get? (When θ=1, the true/exact derivati ve is $\frac{dJ(\theta)}{d\theta} = 6$.)

 * 8 
 * 6
 * 5.9998
 * 6.0002
 
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 4  </font> **  
** <font color=red> $\frac{J(\theta + \epsilon) - J(\theta - \epsilon)}{2\epsilon}= \frac{2*(\theta+\epsilon)^3+2 - \left(2*(\theta-\epsilon)^3+2 \right)}{2\epsilon} $   </font> **  
** <font color=red>  将$\epsilon = 0.01$, $\theta=1$ 代入上式,并化简一下可得出    </font> **  
** <font color=red> $\frac{(\theta+\epsilon)^3 - (\theta-\epsilon)^3}{\epsilon}=\frac{(1+0.01)^3-(1-0.01)^3}{0.01}=6.0002$    </font> **  

---
### 第 4 题
Which of the following statements are true? Check all that apply.


* Using a large value of $\lambda$ cannot hurt the performance of your neural network; the only reason we do not set $\lambda$ to be too large is to avoid numerical problems.
* Gradient checking is useful if we are using gradient descent as our optimization algorithm. However, it serves little purpose if we are using one of the advanced optimization methods (such as in fminunc).
* Using gradient checking can help verify if one's implementation of backpropagation is bug-free.
* If our neural network overfits the training set, one reasonable step to take is to increase the regularization parameter $\lambda$.
 
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 3 4 </font> **  
** <font color=red>  * 选项1: 以前的quiz中遇到过,当选的$\lambda$太大时,会成为一条直线,underfit. 不正确 </font> **  
** <font color=red>  * 选项2: Gradient checking是验检神经网络内部的计算结果对不对,不关心是用的哪个算法,高级算法如fminuc与原始的sigmoid梯度下降都可以用gradient checking来验检. 不正确 </font> **  
** <font color=red>  * 选项3: Gradient checking就是用来验检神经网络内部的计算结果对不对的. 正确 </font> **  
** <font color=red>  * 选项4: 回忆一下当时引入正规化项Regularization的目的是什么? 是为了解决overfitting的问题. 假设设置的$\lambda$太小了就相当于没有加入正规化项,penalize不够,还是会overfit,则需要加大$\lambda$; 再补充另一方面,如果把$\lambda$设置的太大了,就会成为一条直线,导致出现underfit. neural network 与 lr 是一样的. 正确 </font> ** 

---
## 第 5 题
Which of the following statements are true? Check all that apply.

* Suppose that the parameter $\Theta^{(1)}$ is a square matrix (meaning the number of rows equals the number of columns). If we replace $\Theta^{(1)}$ with its transpose $(\Theta^{(1)})^T$, then we have not changed the function that the network is computing.

* Suppose we have a correct implementation of backpropagation, and are training a neural network using gradient descent. Suppose we plot $J(\Theta)$ as a function of the number of iterations, and find that it is increasing rather than decreasing. One possible cause of this is that the learning rate $\alpha$ is too large.

* Suppose we are using gradient descent with learning rate $\alpha$. For logistic regression and linear regression,   
 $J(\Theta)$ was a convex optimization problem and thus we did not want to choose a learning rate $\alpha$ that is too large. 
 For a neural network however, $J(\Theta)$ may not be convex, and thus choosing a very large value of $\alpha$ can only speed up convergence.

* If we are training a neural network using gradient descent, one reasonable "debugging" step to make sure it is working is to plot $J(\Theta)$ as a function of the number of iterations, and make sure it is decreasing (or at least non-increasing) after each iteration.

** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案:  2 4 </font> **   
** <font color=red>  * 选项1: 神经网络的计算(network computing).以第2层为例: $a^{(2)}=g(z^{(2)})=g\left(\Theta^{(1)}*a^{(1)}\right)$, 当$\Theta^{(1)}$转置为$(\Theta^{(1)})^T$时,显然 $g\left(\Theta^{(1)}*a^{(1)}\right) \neq g\left((\Theta^{(1)})^T*a^{(1)}\right)$ . 不正确 </font> **  
** <font color=red>  * 选项2: 当选的$\alpha$太大时,gradient descent有可能越过最低点,导致CostFunction的值越来越大. 正确 </font> **  
** <font color=red>  * 选项3: 没有确定神经网络的$J(\Theta)$是不是一定是凸的(等大神指导),但是就算不是凸的也不一定非得设置一个很大的$\alpha$. 不正确 </font> **  
** <font color=red>  * 选项4: 将CostFunction的值每次都打印出来,看有没有减小来确定我们的训练是不是有效,感觉这个选项是完全正确的废话. 正确 </font> **  

