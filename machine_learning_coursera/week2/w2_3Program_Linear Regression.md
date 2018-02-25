# Week 2 | 3Program_Linear Regression编程解析
### 1. 单变量
#### 1.1 Warm up exercise    10 / 10
写出一个5阶单位矩阵
A = eye(5);
#### 1.2 Compute cost for one variable   40 / 40
写出 损失函数
$J\left( \theta  \right)=\frac{1}{2m}\sum\limits_{i=1}^{m}{{{\left( {{h}_{\theta }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}^{2}}}$的计算,  
在computCost.m中添加:
```python
cost_t = ((X*theta)-y).^2;
J = 1/(2*m)*sum(cost_t);
```

#### 1.3 Gradient descent for one variable   50 / 50
单变量的梯度下降算法:  
```python
for iter = 1:num_iters
    h_theta =  X * theta;
    loss = h_theta - y;
    
    no_sum0 = loss'*X(:,1);
    sum0 = sum(no_sum0);
    theta(1,1) = theta(1,1) - alpha * (1/m) * sum0;
    
    no_sum1 = loss'*X(:,2);
    sum1 = sum(no_sum1);
    theta(2,1) = theta(2,1) - alpha * (1/m) * sum1;
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
```
$\theta_0$的更新过程就是:  
${{\theta }_0}:={{\theta }_0}-\alpha \frac{1}{m}\sum\limits_{i=1}^{m}{{\left( {{h}_{\theta0 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} *x_0^{(i)} \tag{1} $ 
$\theta_1$的更新过程就是:  
${{\theta }_1}:={{\theta }_1}-\alpha \frac{1}{m}\sum\limits_{i=1}^{m}{{\left( {{h}_{\theta1 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} *x_1^{(i)} \tag{2} $ 

* 第1步求${h}_{\theta_0}$: 得到 (nx2)*(2x1)=(nx1)维的列向量  
* 第2步求${h}_{\theta_0}-y$: 得到loss,这是一个 (nx1)维的列向量  
* 第3.1步求 ${{\left( {{h}_{\theta0 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} *x_0^{(i)}$得到no_sum0
* 第3.2步求 ${{\left( {{h}_{\theta0 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} *x_1^{(i)}$得到no_sum1
* 第4步分别求和
* 第5步计算最后的 $\theta0$ 与 $\theta1$  

---
### 2. 多变量
第1步先把数值归一化   
第2步利用多变量的梯度下降法计算$\theta$,并预测(1650,3)的y  
第3步利用正规化方程法计算$\theta$,并预测(1650,3)的y    
第4步比较两种方法的结果并画出损失函数曲线    
#### 2.1 Feature normalization   0 / 0
为了使收敛速度加快,需要对所有的变量进行归一化处理。几种归一化的方法:

* a. 线性函数转换: y=(x-MinValue)/(MaxValue-MinValue)  --> 在测试中用到过
* b. 对数函数转换: y=log10 (x)  
* c. 反余切函数转换: y=arctan(x)*2/PI
* d. 0均值归一化方法: 减去均值，除以方差: y=(x-means)/variance --> 这儿
0均值标准化方法会将原始数据集归一化为均值为0,方差1的数据集  
```python
for i=1:size(X,2),
  fprintf("i= %d\n", i);
  mu(i) = mean(X(:,i));       --> 对这一列先求均值
  sigma(i) = std(X(:,i));     --> 对这一列再求方差
  X_norm(:,i) = (X(:,i) - mu(i) ) /sigma(i); --> 对这一列的每个值代入公式求得
end;
```
注意: octave对矩阵做加减法并不需要相同的nxm列的,只需要一个数就可以了  

#### 2.2 Compute cost for multiple variables 0 / 0


#### 2.3 Gradient descent for multiple variables 0 / 0
```python
for iter = 1:num_iters
    predictions =  X * theta;
    updates = X' * (predictions - y);
    theta = theta - alpha * (1/m) * updates;

    J_history(iter) = computeCostMulti(X, y, theta);
end
```
$\theta_0$的更新过程就是:  
${{\theta }_0}:={{\theta }_0}-\alpha \frac{1}{m}\sum\limits_{i=1}^{m}{{\left( {{h}_{\theta0 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} *x_0^{(i)} $ 

$\sum\limits_{i=1}^{m}{{\left( {{h}_{\theta0 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} *x_0^{(i)}$
把 ${{\left( {{h}_{\theta0 }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}} \right)}} $ 记作列向量A, 则这个求和
$A_1*x_0^{1}+A_2*x_0^{2}+A_3*x_0^{3}+....+A_n*x_0^{n}$ 即$X^T$的第1行与向量$A$的乘积  
** 注意: computeCostMulti 别忘记在 computeCostMulti.m中修改一下,跟单变量一样 **
##### 2.3.1 使用梯度下降进行预测
```python
price = 0;
element = [1,(1650 - mu(1))/sigma(1),(3 - mu(2))/sigma(2)];
price = element * theta;
```
先把数据作归一化,然后代到求得$\theta$的公式中,计算出最终的price  
#### 2.4 Normal equations
正规化方程法,直接代公式计算  
$\theta =(X^TX)^{-1}X^Ty$ 
```python
theta = pinv(X' * X) * X' * y;
``` 
函数pinv是求逆  X上面跟着 '是转置  
##### 2.4.1  使用正规化方程法进行预测
```python
price = 0; 
element = [1,1650,3];
price = element * theta;
```
直接代公式计算就可以了

---
#### 最终
```python
==
==                                   Part Name |     Score | Feedback
==                                   --------- |     ----- | --------
==                            Warm-up Exercise |  10 /  10 | Nice work!
==           Computing Cost (for One Variable) |  40 /  40 | Nice work!
==         Gradient Descent (for One Variable) |  50 /  50 | Nice work!
==                       Feature Normalization |   0 /   0 | Nice work!
==     Computing Cost (for Multiple Variables) |   0 /   0 | Nice work!
==   Gradient Descent (for Multiple Variables) |   0 /   0 | Nice work!
==                            Normal Equations |   0 /   0 | Nice work!
==                                   --------------------------------
==                                             | 100 / 100 |
```