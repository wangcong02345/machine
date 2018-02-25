# w4_2Multi-class Classification and Neural Networks编程解析
### 1. ex3.m
#### 1.1  ex3.m框架分析
把数据可视化, 在plotData.m中添加:
```python
input_layer_size  = 400;  % 20x20 Input Images of Digits
num_labels = 10;          % 10 labels, from 1 to 10
                          % (note that we have mapped "0" to label 10)

# 第1步加载数据并显示,是里面有各种手写0-9的数字网格
load('ex3data1.mat'); % training data stored in arrays X, y
m = size(X, 1);
rand_indices = randperm(m);
sel = X(rand_indices(1:100), :);
displayData(sel);


#第2.1步 Vectorize Logistic Regression 
theta_t = [-2; -1; 1; 2];
X_t = [ones(5,1) reshape(1:15,5,3)/10];
y_t = ([1;0;1;0;1] >= 0.5);
lambda_t = 3;
[J grad] = lrCostFunction(theta_t, X_t, y_t, lambda_t);

# 第2.2 步 实现one-vs-All Training, 将手写的0-9图片区分出来
lambda = 0.1;
[all_theta] = oneVsAll(X, y, num_labels, lambda);

# 第3步进行预测
pred = predictOneVsAll(all_theta, X);
```
#### 1.2  Regularized logistic regression 0 / 30
分两步,先计算$J(\theta)$ 再计算$\theta$  
##### 1.2.1 logistic regression Cost Function
带正则化项的logistic回归的损失函数:   
$J\left( \theta  \right)=\frac{1}{m}\sum\limits_{i=1}^{m}{\left[-{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}}) \right)-\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}}) \right)\right]}+\frac{\lambda }{2m}\sum\limits_{j=1}^{n}{\theta _{j}^{2}}$  
```python
h_theta = sigmoid(X*theta);
left = -(y'*log(h_theta));
right = (1-y)'*log(1-h_theta);
theta_line_num = length(theta);
reg = sum(theta(2:theta_line_num,:) .^ 2);
J = 1/m*(left-right)+lambda/(2*m)*reg;
```
* 第1行: 先计算$h_\theta$, 注意这儿的sigmoid函数己经写好了,在文件sigmoid.m中  
* 第2行: 计算左半部分left=$\sum\limits_{i=1}^{m} -{{y}^{(i)}}\log \left( {{h}_{\theta }}( {{x}^{(i)}}) \right)$
* 第3行: 计算右半部分right=$\sum\limits_{i=1}^{m}\left( 1-{{y}^{(i)}} \right)\log \left( 1-{{h}_{\theta }}( {{x}^{(i)}}) \right)$
* 第4行: 计算列向量theta的长度: 因为$\theta$是(28x1)的列向量,$\theta_0$不作为penalty项,所以要剔除
* 第5行: 从列向量theta的第2行到最后一行取平方,再求和,得到正则化项
* 第6行: 将上述的left right reg,代入到公式,即可求得$J(\theta)$

##### 1.2.2 Gradient for regularized LR  
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


#### 1.3 One-vs-all classifier training  0 / 20
实现 oneVsAll函数, 在oneVsAll.m中 
```python
initial_theta = zeros(n + 1, 1);
options = optimset('GradObj', 'on', 'MaxIter', 50);
for c=1:num_labels,
  theta = fmincg (@(t)(lrCostFunction(t, X, (y == c), lambda)), initial_theta, options);
  all_theta(c,:) = theta';
end;
```
其中fmincg函数的实现是在 fmincg.m 中, 上面函数直接抄的提示中的实现.    
#### 1.4 One-vs-all classifier prediction    0 / 20
在 predictOneVsAll.m中实现  
```python
all_preds = all_theta * X';
[max_vals, max_ndxs] = max(all_preds);
p = max_ndxs';
```

### 2. ex3_nn.m 
#### 2.1  ex3_nn.m框架分析
```python
%% Setup the parameters you will use for this exercise


#第1步加载数据并显示
load('ex3data1.mat');
m = size(X, 1);
sel = randperm(size(X, 1));
sel = sel(1:100);
displayData(X(sel, :));

input_layer_size  = 400;  % 20x20 Input Images of Digits
hidden_layer_size = 25;   % 25 hidden units
num_labels = 10;          % 10 labels, from 1 to 10   
                          % (note that we have mapped "0" to label 10)
# 第2步加载参数
load('ex3weights.mat');

# 第3步进行预测
pred = predict(Theta1, Theta2, X);

#第4步显示预测结果
rp = randperm(m);
for i = 1:m
    displayData(X(rp(i), :));
    pred = predict(Theta1, Theta2, X(rp(i),:));
    # 按q退出
    s = input('Paused - press enter to continue, q to exit:','s');
    if s == 'q'
      break
    end
end
```

#### 2.2 Neural network prediction function    0 / 30

### 3. 总结
#### 3.1 
