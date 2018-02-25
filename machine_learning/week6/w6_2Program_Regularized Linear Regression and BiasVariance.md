# w6_2Regularized Linear Regression and BiasVariance编程解析
### 1. ex5 流程分析
#### 1.1  plotData
按照ex5.m中的流程走一遍
```python


```

### 2. 编程分析
#### 2.0 计算公式
代价函数：  
${{h}_{\theta }}\left( x \right)=\frac{1}{2m}\sum\limits_{i=1}^{m}\left(h\theta(x^{(i)}-y^{(i)}\right)^2 +\frac{\lambda}{2m}\left(\sum\limits_{j=1}^{n}\theta_j^2\right)$  
$\theta$的更新(分j=0的情况与$j \geq 1$两种情况):  
$\frac{\partial J\left( \theta  \right)}{\partial {{\theta }_{j}}}=\frac{1}{m}\sum\limits_{i=1}^{m}{\left({{h}_{\theta }}( {{x}^{(i)}} )-{{y}^{(i)}}\right)x_{_{j}}^{(i)}}\tag {j=0}$  
$\frac{\partial J\left( \theta  \right)}{\partial {{\theta }_{j}}}=\frac{1}{m}\sum\limits_{i=1}^{m}{\left({{h}_{\theta }}( {{x}^{(i)}} )-{{y}^{(i)}}\right)x_{_{j}}^{(i)}} + \frac{\lambda}{m}\theta_j\tag {j>=1}$ 

#### 2.1 Regularized linear regression cost function 0 / 25
X=12x2 theta=2x1 y=12x1  
根据上面2.0的计算公式,在linearRegCostFunction.m中添加:  
```python
# 第1步计算cost
h_theta = X * theta ;
epsilon = h_theta - y;
left = (1/(2*m))*sum(epsilon .^ 2);
right = (lambda/(2*m))*sum(theta(2:end) .^ 2);
J = left + right;
```

#### 2.2 Regularized linear regression gradient  0 / 25
根据上面2.0的计算公式,在linearRegCostFunction.m中添加:  
```python
# 第2步计算grad
grad = (1/m)*X'*epsilon;
grad(2:end) += (lambda/m)*theta(2:end);
```

#### 2.3 Learning curve  0 / 20 
在learningCurve.m中添加:  
```python
for i = 1:m
  x_train = X(1:i,:);
  y_train = y(1:i);
  theta = trainLinearReg(x_train, y_train, lambda); 
  [J_train, grad_train]=linearRegCostFunction(x_train,y_train,theta, 0); 
  [J_cross, grad_cross]=linearRegCostFunction(Xval,yval,theta, 0);
  error_train(i) = J_train;
  error_val(i) = J_cross;
end
```
<font color=red> ** 交叉验证部分的数据己经读到Xval与yval中 ** </font>   

#### 2.4 Polynomial feature mapping  0 / 10
X_poly(i, :) = [X(i) X(i).^2 X(i).^3 ...  X(i).^p];
xp的第1列 = X的第1列的1次方   
xp的第2列 = X的第2列的2次方   
xp的第3列 = X的第3列的3次方   
xp的第4列 = X的第3列的4次方   
要实现如上的效果
```python
for i=1:p
  X_poly(:, i) = X(:,1).^i;
end
```
#### 2.5 Cross validation curve  0 / 20
在validationCurve.m 中  
```python
for i = 1:length(lambda_vec)
    lambda = lambda_vec(i);
    theta = trainLinearReg(X, y, lambda);
    [J_train, grad_train]=linearRegCostFunction(X, y, theta, 0); 
    [J_cross, grad_cross]=linearRegCostFunction(Xval, yval, theta, 0);
    error_train(i) = J_train;
    error_val(i) = J_cross;
end
```

### 3. 总结
1 Regularized linear regression cost function 0 / 25
2 Regularized linear regression gradient  0 / 25
3 Learning curve  0 / 20
4 Polynomial feature mapping  0 / 10
5 Cross validation curve  0 / 20

