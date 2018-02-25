# w5_2Neural Network Learning编程解析
### 1. ex4 流程分析
#### 1.1  plotData
按照ex4.m中的流程走一遍
```python
%% Setup the parameters you will use for this exercise
input_layer_size  = 400;  % 20x20 Input Images of Digits
hidden_layer_size = 25;   % 25 hidden units
num_labels = 10;          % 10 labels, from 1 to 10   
                          % (note that we have mapped "0" to label 10)

%% =========== 第1步加载数据并将数据可视化 =============
load('ex4data1.mat');
m = size(X, 1);
sel = randperm(size(X, 1));
sel = sel(1:100);
displayData(X(sel, :));

%% ================ 第2步加载参数 ================
% Load the weights into variables Theta1 and Theta2
load('ex4weights.mat');
% Theta1(25x401) Theta2(10x26)
% nn_params=25x401+10x26=10285
nn_params = [Theta1(:) ; Theta2(:)];

%% ================ 第3步: Compute Cost (Feedforward) ================
lambda = 0;
% nn_params=25x401+10x26=10285, input_layer_size=400,hidden_layer_size=25
% num_labels=10, X=5000x400的图像, y=5000*1
J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, ...
                   num_labels, X, y, lambda);

%% =============== Part 4: Implement Regularization ===============
lambda = 1;
J = nnCostFunction(nn_params, input_layer_size, hidden_layer_size, ...
                   num_labels, X, y, lambda);

%% ================ Part 5: Sigmoid Gradient  ================
g = sigmoidGradient([-1 -0.5 0 0.5 1]);

%% ================ Part 6: Initializing Pameters ================
initial_Theta1 = randInitializeWeights(input_layer_size, hidden_layer_size);
initial_Theta2 = randInitializeWeights(hidden_layer_size, num_labels);
initial_nn_params = [initial_Theta1(:) ; initial_Theta2(:)];


%% =============== Part 7: Implement Backpropagation ===============
checkNNGradients;

%% =============== Part 8: Implement Regularization ===============
lambda = 3;
checkNNGradients(lambda);
debug_J  = nnCostFunction(nn_params, input_layer_size, ...
                          hidden_layer_size, num_labels, X, y, lambda);

%% =================== Part 8: Training NN ===================
options = optimset('MaxIter', 50);
lambda = 1;

costFunction = @(p) nnCostFunction(p, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, X, y, lambda);

[nn_params, cost] = fmincg(costFunction, initial_nn_params, options);

Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

%% ================= Part 9: Visualize Weights =================
displayData(Theta1(:, 2:end));

%% ================= Part 10: Implement Predict =================
pred = predict(Theta1, Theta2, X);
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
function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
% nn_params就是传入的 Theta1 与 Theta2
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));
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


1   Feedforward and cost function   0 / 30
2   Regularized cost function   0 / 15
3   Sigmoid gradient    0 / 5
4   Neural net gradient function (backpropagation)  0 / 40
5   Regularized gradient    0 / 10
