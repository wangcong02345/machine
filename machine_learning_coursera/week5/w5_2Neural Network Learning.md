# w5_2Neural Network Learning编程解析
### 1. ex4 流程分析
#### 1.1  plotData
按照ex4.m中的流程走一遍
```python
%% Setup the parameters you will use for this exercise
input_layer_size  = 400;  % 第1层inputLayer有400个input,因Image有20x20=400个像素
hidden_layer_size = 25;   % 第2层hiddenLayer有25个hidden units
num_labels = 10;          % 第3层输出层有10 labels, from 1 to 10   
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
### 2. 编程解析 
#### 2.1  先看一下Sigmoid function 的公式
sigmoid 函数公式为： 
$g\left( z \right)=\frac{1}{1+{{e}^{-z}}} \tag 1$  
逻辑回归模型的假设函数$h_\theta$：  
  ${{h}_{\theta }}\left( x \right)=\frac{1}{1+{{e}^{-{{\theta }^{T}}X}}} \tag 2$  
costFunction:  
$J\left( \theta  \right)=\frac{1}{m}\sum\limits_{i=1}^{m}{\left[-{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}} ) \right)-\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}} ) \right)\right]} \tag 3$ 
加入正则化的代价函数:  
$J\left( \theta  \right)=\frac{1}{m}\sum\limits_{i=1}^{m}{\left[-{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}} ) \right)-\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}} ) \right)\right]}+\frac{\lambda }{2m}\sum\limits_{j=1}^{n}{\theta _{j}^{2}} \tag 4$ 
$\theta$的更新:  
$\frac{\partial J\left( \theta  \right)}{\partial {{\theta }_{j}}}=\frac{1}{m}\sum\limits_{i=1}^{m}{({{h}_{\theta }}\left( {{x}^{(i)}} \right)-{{y}^{(i)}})x_{_{j}}^{(i)}} \tag 5$  
#### 2.2  神经网络的公式
costFunction:  
$J\left( \theta  \right)=\frac{1}{m}\sum\limits_{i=1}^{m}\sum\limits_{k=1}^{K}{\left[-{{y}_k^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}} )_k \right)-\left( 1-{{y}_k^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}} )_k \right)\right]}+$  
$\frac{\lambda }{2m}\left[\sum\limits_{j=1}^{25}\sum\limits_{k=1}^{400}(\Theta_{(j,k)}^{(1)})^2+ \sum\limits_{j=1}^{25}\sum\limits_{k=1}^{400}(\Theta_{(j,k)}^{(2)})^2\right]  \tag 1$ 
#### 2.3 Feedforward and cost function   0 / 30 
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
% 1. 正向传播,计算各个值
% 先给X扩充一个全为1的列  X=5000x400 变为 X=5000x401 Theta1(25x401) Theta2(10x26)   
X = [ones(m,1) X];  
% 则layer2就是 Theta.*X的转置 = (25x401).*(401x5000) = (25x5000)
z2 = Theta1 *  X'
a2 = sigmoid(z2)

% get layer 3
X2 = [ones(m,1) a2']; %X2=(5000x26)
z3 = Theta2 * X2';  %(10x26)*(26x5000)
a3 = sigmoid(z3);   %a3=(10x5000)

% 第2步 将y(5000x1)扩展成(5000x10): 
% y[0]=10 意思是y_expand的第0列第10行值为1
% y[1]=3 意思是y_expand的第1列第3行值为1
y_expand = zeros(num_labels, m);
for i=1:m,
  y_expand(y(i), i) = 1;
end

% 第4步: 代入公式计算J
left = -y_expand .* log(a3);
right = (1-y_expand) .* log(1-a3);
J = (1/m)*sum(sum(left-right));
```
此时输出J=0.287629

#### 2.4 Regularized cost function   0 / 15
正则项部分的公式: $\frac{\lambda }{2m}\left[\sum\limits_{j=1}^{25}\sum\limits_{k=1}^{400}(\Theta_{(j,k)}^{(1)})^2+ \sum\limits_{j=1}^{25}\sum\limits_{k=1}^{400}(\Theta_{(j,k)}^{(2)})^2\right]  \tag 3$ 

```python
% Theta1(25x401) Theta2(10x26)
Theta1_pow = Theta1(:,2:end).^2;
Theta2_pow = Theta2(:,2:end).^2;
Theta_sum = sum(sum(Theta1_pow)) + sum(sum(Theta2_pow));
reg = lambda/(2*m)*Theta_sum;
J = J + reg;
```
加入正则化项之后J=0.383770
#### 2.5 Sigmoid gradient    0 / 5
```python
function g = sigmoidGradient(z)
g = zeros(size(z));
% 
g = sigmoid(z) .* (1 - sigmoid(z));
end
```
#### 2.6  Neural net gradient function (backpropagation)  0 / 40
调用函数 checkNNGradients
先初始化Theta1(5x4)  Theta2(3x6)   X(5x3)  y(5x1)  
nn_params(38=Theta1+Theta2)  
```python
% 2. backpropagation
for t=1:m,

    % dummie pass-by-pass
    % forward propag

    a1 = X(t,:); % X already have bias
    z2 = Theta1 * a1';

    a2 = sigmoid(z2);
    a2 = [1 ; a2]; % add bias

    z3 = Theta2 * a2;

    a3 = sigmoid(z3); % final activation layer a3 == h(theta)


    % back propag (god bless me)    

    z2=[1; z2]; % bias

    delta_3 = a3 - y_expand(:,t); % y_expand trick - getting columns of t element
    delta_2 = (Theta2' * delta_3) .* sigmoidGradient(z2);

    % skipping sigma2(0) 
    delta_2 = delta_2(2:end); 

    Theta2_grad = Theta2_grad + delta_3 * a2';
    Theta1_grad = Theta1_grad + delta_2 * a1; % I don't know why a1 doesn't need to be transpost (brute force try)

end;

Theta1_grad = Theta1_grad ./ m;
Theta2_grad = Theta2_grad ./ m;
```


#### 2.7 Regularized gradient    0 / 10
```python
% 需要先把上面两行注掉
% Theta1_grad = Theta1_grad ./ m;
% Theta2_grad = Theta2_grad ./ m;


% Regularization (here you go)
    Theta1_grad(:, 1) = Theta1_grad(:, 1) ./ m;
    Theta1_grad(:, 2:end) = Theta1_grad(:, 2:end) ./ m + ((lambda/m) * Theta1(:, 2:end));
    Theta2_grad(:, 1) = Theta2_grad(:, 1) ./ m;
    Theta2_grad(:, 2:end) = Theta2_grad(:, 2:end) ./ m + ((lambda/m) * Theta2(:, 2:end));
```

#### 2.7 
randInitializeWeights()--> 这个函数目前全返回0  
initial_Theta1 是 25x401, 全为0  
initial_Theta2 是 10x26  
initial_nn_params 是 25x401+10x26=10285  <unrolling> 


### 4. 补充Octave:
#### 4.1 增加全为1的列
```java
octave:1> A=[1 2 3; 4 5 6]
A =
   1   2   3
   4   5   6

octave:2> B=[ones(2, 1) A]
B =
   1   1   2   3
   1   4   5   6
```

#### 2.2 对于矩阵的 .* 与 *
```java
octave:8> A
A =
   1   2   3
   4   5   6
octave:9> B
B =
   2   3   4
   5   6   7
octave:10> A * B
error: operator *: nonconformant arguments (op1 is 2x3, op2 is 2x3)
octave:10> A .* B
ans =
    2    6   12
   20   30   42
octave:11> A * B'
ans =
   20   38
   47   92
```
#### 2.3 对于矩阵的 sum
```python
octave:12> A
A =
   1   2   3
   4   5   6
octave:13> sum(A)   --> 把每一列求和
ans =   5   7   9
octave:14> sum(sum(A))
ans =  21
```
### 3. 总结


1   Feedforward and cost function   0 / 30
2   Regularized cost function   0 / 15
3   Sigmoid gradient    0 / 5
4   Neural net gradient function (backpropagation)  0 / 40
5   Regularized gradient    0 / 10
