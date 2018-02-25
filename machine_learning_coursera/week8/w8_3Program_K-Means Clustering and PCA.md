# Week8_3Program_K-Means Clustering and PCA编程解析
### 1. ex7 流程分析
#### 1.1  plotData
按照ex7.m中的流程走一遍
```python


```

### 2. 编程分析
#### 2.1 Find closest centroids  0 / 30
计算公式: $||x^{(i)}- \mu_j||^2$  
X=(300x2)  K=3  centroids=(3x2) idx=(300x1)  
在 findClosestCentroids.m 中添加  
```python
distance = zeros(K, 1);
for i = 1:length(idx)    
    for j = 1:K
        diff = (X(i,:) - centroids(j,:)) .^ 2;
        distance(j) = sum(sum(diff));       
    endfor
    [value, idx(i)] = min(distance);
endfor
```
每一行的2个数,代表着一个点的(x,y)坐标   
a. diff 行就是求两个值之间的差  
X=[1 2; 3 4; 5 6; .....]  u=[3 3; 6 2; 8 5];  
则diff行就是 1-7 2-8 = -6 -6, 再求平方 36 36  
b. X中的第1行(1,2)与u中的每个向量执行a的操作  
c. 最后两个sum,先对列求和,再对行求和,就是distance了  
   distance[1]是x1与u1的差
   distance[2]是x2与u2的差
   distance[3]是x3与u3的差
d. 求数组distance中的最小值,及其索引  
其中value是最小的值, idx(i)是最小值的索引    

#### 2.2 Compute centroid means  0 / 30  
计算公式: $\mu_k := \frac{1}{|C_k|}\sum\limits_{i \in C_k}x^{(i)}$  
X=(300x2)  K=3  centroids=(3x2) idx=(300x1)   
计算公式:    
X=(300x2)  K=3  centroids=(3x2) idx=(300x1)  
在 computeCentroids.m 中添加:   
```python
for k = 1:K
    xPos = find(idx == k);
    if(size(xPos,1)>0)
      avg = mean(X(xPos,:));
      centroids(k, :) = avg;
end
```
<font color="red"> **  将距离u1最近的找出来,取个平均值作为新的u1 ** </font>    
<font color="red"> ** 将距离u2最近的找出来,取个平均值作为新的u2  ** </font>   
<font color="red"> ** 将距离u3最近的找出来,取个平均值作为新的u3  ** </font>   
<font color="red"> ** 当k=1时, xPos行就是找到距u1最近的下标索引  ** </font>   
<font color="red"> ** a. 将这些下标索引带回到X中去, 找到这些点  ** </font>   
<font color="red"> ** b.将这些点的x坐标取平均值作为新的u1的x坐标 ** </font>   
<font color="red"> ** c. 将这些点的y坐标取平均值作为新的u1的y坐标 ** </font>
### 3. PCA
#### 3.1  PCA 0 / 20
featureNormalize在PCA之前先Normalize过了  
计算公式:   
协方差covariance Matrix=$\Sigma := \frac{1}{m}X^TX$  
SVD= [U, S, V] = svd(Sigma)
```python
sigma = (X' * X) ./ m;
[U, S, V] = svd(sigma);
```
用octave自带的svd函数

#### 3.2 Project data  0 / 10
在projectData.m中添加:  
```python
subsetU = U(:, 1:K);
Z = X * subsetU;
```
#### 3.3 Recover data  0 / 10
在recoverData.m中添加:  
```python
subsetU = U(:, 1:K);
X_rec = Z * subsetU';
```
### 3. 总结
1 Find closest centroids  0 / 30
2 Compute centroid means  0 / 30
3 PCA 0 / 20
4 Project data  0 / 10
5 Recover data  0 / 10



