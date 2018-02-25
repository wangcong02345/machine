# w3_3Program_Logistic Regression编程解析
### 1. Logistic Regression
#### 1.1  plotData
把数据可视化, 在plotData.m中添加:
```python
% Find Indices of Positive and Negative Examples
pos = find(y==1); neg = find(y == 0);
% Plot Examples
plot(X(pos, 1), X(pos, 2), 'k+','LineWidth', 2, 'MarkerSize', 3);
plot(X(neg, 1), X(neg, 2), 'ko', 'MarkerFaceColor', 'y', 'MarkerSize', 3);
```
#### 1.2 Sigmoid function  0 / 5
sigmoid 函数公式为： 
$g\left( z \right)=\frac{1}{1+{{e}^{-z}}}$  
逻辑回归模型的假设函数：  
  ${{h}_{\theta }}\left( x \right)=\frac{1}{1+{{e}^{-{{\theta }^{T}}X}}}$  
在plotData.m中添加:
```python
g = 1 ./(1+exp(-z))
```

#### 1.3 Gradient for logistic regression  0 / 30
costFunction:  
$J\left( \theta  \right)=\frac{1}{m}\sum\limits_{i=1}^{m}{[-{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}}) \right)-\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}({{x}^{(i)}}) \right)]}$  

$\theta$的更新:  
$\frac{\partial J\left( \theta  \right)}{\partial {{\theta }_{j}}}=\frac{1}{m}\sum\limits_{i=1}^{m}{({{h}_{\theta }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}})x_{_{j}}^{(i)}}$  


``` python
h_theta = sigmoid(X*theta);
left = -(y')*log(h_theta);
right = (1-y)'*log(1-h_theta);
J = 1/m*(left-right);
grad = (h_theta-y)' *X;
grad = grad*(1/m);
```

计算过程:   
n=2 --> 有2个feature  
m=100 --> 有100个样本  
X是(100x3)的矩阵 &nbsp;&nbsp;  $\theta$是(3x1)的向量 &nbsp;&nbsp; y是(100x1)的向量  
第1行: 先求$h_\theta=sigmoid(X*\theta)$, 得出一个(100x1)的向量  
第2行: left=$\sum\limits_{i=1}^{m} \left( -{{y}^{(i)}}\log ( {{h}_{\theta }}( {{x}^{(i)}}) ) \right)$,left是一个数值  
第3行: right=$\sum\limits_{i=1}^{m} \left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}({{x}^{(i)}}) \right)$ right是一个数值  
第4行: (left-right)的差再乘以 $\frac{1}{m}$ 就得到了 $J(\theta)$

#### 1.4 Predict function  0 / 5
对训练的数据进行预测,并与结果y进行比较看正确率
在predict.m中加入:  
```python
h_theta = X*theta;
h_theta = sigmoid(h_theta);
p = round(h_theta);
```
预测函数 $h_\theta=g(X\theta)$,其中g(x)是sigmoid函数  
第1 2行: 对每个样本进行预测,得出预测的结果,  X(100x3)*theta(3x1)=h_theta(100x1)   
第3行: 如果结果大于0.5则为1, 若结果<0.5则为0, round操作  

###2 Regularized logistic regression
#### 2.1 说明一下mapFeature的作用  
在 mapFeature.m 中  
``` python
function out = mapFeature(X1, X2)  
degree = 6;
out = ones(size(X1(:,1)));
for i = 1:degree
    for j = 0:i
        out(:, end+1) = (X1.^(i-j)).*(X2.^j);
    end
end
end
```
新的feature 矩阵是这种形式: 按列来看  

* 第1列全为1  
* 当i=1时产生2列: $x_1$与$x_2$    
* 当i=2时产生3列: $x_1^2$ , $x_1x_2$ , $x_2^2$  
* 当i=3时产生4列: $x_1^3$ , $x_1^2x_2$ , $x_1x_2^2$, $x_2^3$   
*  ...  
* 当i=6时产生7列: $x_1^6$ , $x_1^5x_2$ , $x_1^4x_2^2$,  ..., $x_2^6$     
把上面的28列排起来,则:  
  mapFeature(x) = $\left(1\quad x_1 \quad x_2 \quad x_1^2 \quad x_1x_2 \quad x_2^2 \quad x_1^3 \quad x_1^2x_2 \quad x_1x_2^2 \quad x_2^3\quad .... \quad x_2^6\right)$其中的每一项代表一列  

#### 2.2 说明一下总体的框架
```python
# 第1步,先把数据从ext2data2.txt中读取出来,并图像显示出来
# X是前两列(118x2), y是结果(118x1)
data = load('ex2data2.txt');
X = data(:, [1, 2]); y = data(:, 3);
plotData(X, y);

# 第2步,调用mapFeatutre.m中的mapFeature
# X是(118x28)
X = mapFeature(X(:,1), X(:,2));

# 按照X的列来取theta的项,所以theta是(28x1)
initial_theta = zeros(size(X, 2), 1);

# 将lambda设为1 
lambda = 1;
# 计算 theta
[cost, grad] = costFunctionReg(initial_theta, X, y, lambda);
test_theta = ones(size(X,2),1);
# 最后进行预测
p = predict(theta, X);
```
#### 2.3 Compute cost for regularized LR 0 / 15
正则化代价函数:   
$J\left( \theta  \right)=\frac{1}{m}\sum\limits_{i=1}^{m}{\left[-{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}}) \right)-\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}}) \right)\right]}+\frac{\lambda }{2m}\sum\limits_{j=1}^{n}{\theta _{j}^{2}}$  
```python
h_theta = sigmoid(X*theta);
left = -(y'*log(h_theta));
right = (1-y)'*log(1-h_theta);
theta_line_num = length(theta)
reg = sum(theta(2:theta_line_num,:) .^ 2);
J = 1/m*(left-right)+lambda/(2*m)*reg;
```
* 第1行: 先计算$h_\theta$
* 第2行: 计算左半部分left=$\sum\limits_{i=1}^{m} -{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}}) \right)$
* 第3行: 计算右半部分right=$\sum\limits_{i=1}^{m}\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}}) \right)$
* 第4行: 计算列向量theta的长度: 因为$\theta$是(28x1)的列向量,$\theta_0$不作为penalty项,所以要剔除
* 第5行: 从列向量theta的第2行到最后一行取平方,再求和,得到正则化项
* 第6行: 将上述的left right reg,代入到公式,即可求得$J(\theta)$

#### 2.4 Gradient for regularized LR 0 / 15
下面计算grad:  
```python
h_theta = sigmoid(X*theta);  --> 这个上面己经有了
left_grad = X' * (h_theta-y);
grad = 1/m*left_grad + lambda/m*theta;
grad(1) = 1/m*(X(:,1))'*(h_theta-y);
```
$\theta$的更新公式：   
$\frac{\partial J\left( \theta  \right)}{\partial {{\theta }_{j}}}= \left( \frac{1}{m}\sum\limits_{i=1}^{m}{({{h}_{\theta }}( {{x}^{(i)}} )-{{y}^{(i)}})x_{_{j}}^{(i)}} \right)+ \frac{\lambda}{m}\theta_j \quad for\  j \ge 1$  
$\frac{\partial J\left( \theta  \right)}{\partial {{\theta }_{j}}}= \left( \frac{1}{m}\sum\limits_{i=1}^{m}{({{h}_{\theta }}( {{x}^{(i)}} )-{{y}^{(i)}})x_{_{j}}^{(i)}} \right)  \quad for \  j= 1$  

* 第1行: 先计算$h_\theta$,这个上面己经有了
* 第2,3行: 先计算左括号的部分,然后加上正则化项
* 第4行: 再单独计算$\theta_0$,也就是代码里面的grad(1)  


### 3. 总结
