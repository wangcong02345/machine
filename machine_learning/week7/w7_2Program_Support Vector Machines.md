# Week7_2Program_Support Vector Machines编程解析
### 1. ex6 流程分析
#### 1.1  plotData
按照ex6.m中的流程走一遍
```python


```

### 2. 编程分析
#### 2.0 计算公式
${{h}_{\theta }}\left( x \right)=\min\limits_{\theta} C\sum\limits_{i=1}^{m}\left[y^{(i)}cost_1(\theta^T x^{(i)})+(1-y^{(i)})cost_0(\theta^Tx^{(i)})\right]+\frac{1}{2}\sum\limits_{i=1}^{n}\theta_j^2$  

#### 2.1 Gaussian kernel 0 / 25
高斯核函数的计算公式:  
$\begin{align*} \\& K \left( x, z \right) = \exp \left( - \dfrac{\| x - z \|^{2}}{2 \sigma^{2}} \right) \end{align*}$
在 gaussianKernel.m 中添加:  
```python
sim = exp(-sum((x1-x2).^2)/(2*sigma^2));
```

#### 2.2 Parameters (C, sigma) for dataset 3 0 / 25
多用几组参数来进行测试: 
ex7.pdf中给出了8个paramers  
```python
paramList = [0.01, 0.03, 0.1, 0.3,  1, 3, 10, 30];
results = [];

for C = paramList,
    for sigma = paramList,       
      model= svmTrain(X, y, C, @(x1, x2) gaussianKernel(x1, x2, sigma)); 
      pred = svmPredict(model, Xval);      
      testError = mean(double(pred ~= yval));      
      fprintf("C: %f\nsigma: %f\nerror: %f\n", C, sigma, testError);      
      results = [results; C, sigma, testError];      
    end
end
[minError, minIndex] = min(results(:,3));
C = results(minIndex,1);
sigma = results(minIndex,2);
```

### 3. 垃圾邮件分类
#### 3.1  Email preprocessing 0 / 25
在 processEmail.m 中添加:   
```python
word_indices = [word_indices; find(ismember(vocabList, str))];
```

#### 2.4 Email feature extraction    0 / 25
在 emailFeatures.m 中添加:  
```python
x(word_indices)=1;
```

### 3. 总结
1   Gaussian kernel 0 / 25
2   Parameters (C, sigma) for dataset 3 0 / 25
3   Email preprocessing 0 / 25
4   Email feature extraction    0 / 25


