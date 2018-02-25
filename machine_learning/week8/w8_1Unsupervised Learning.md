# Week8_1Unsupervised Learning

### 第 1 题
For which of the following tasks might K-means clustering be a suitable algorithm? Select all that apply.  

* Given a database of information about your users, automatically group them into different market segments.
* Given sales data from a large number of products in a supermarket, figure out which products tend to form coherent groups (say are frequently purchased together) and thus should be put on the same shelf.  
* Given historical weather records, predict the amount of rainfall tomorrow (this would be a real-valued output)  
* Given sales data from a large number of products in a supermarket, estimate future sales for each of these products.

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 2  K-Means用来分类的,不能做预测 </font> **   
** <font color=red> 选项1: 把客户按市场分类,可以作到. 正确 </font> **   
** <font color=red> 选项2: 给出超市商品的销售数据,把卖的最快的商品与卖的不快的商品进行分类. 正确 </font> **   
** <font color=red> 选项3: 给出天气的历史数据,预测明天的天气,不能进行预测,做不到. 不正确 </font> **   
** <font color=red> 选项4: 给出超市商品的销售数据, 预测未来的销量,做不到. 不正确 </font> **   

* Given a set of news articles from many different news websites, find out what are the main topics covered.  
* Given many emails, you want to determine if they are Spam or Non-Spam emails. 
* From the user usage patterns on a website, figure out what different groups of users exist.  
* Given historical weather records, predict if tomorrow's weather will be sunny or rainy.  
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 3  K-Means用来分类的,不能做预测 </font> ** 

---
### 第 2 题
Suppose we have three cluster centroids $\mu_1 = \begin{bmatrix}1 \\ 2 \end{bmatrix}$ $\mu_2 = \begin{bmatrix}-3 \\ 0 \end{bmatrix}$ and $\mu_3 = \begin{bmatrix}4 \\ 2 \end{bmatrix}$.  Furthermore, we have a training example $x^{(i)} = \begin{bmatrix}-2 \\ 1 \end{bmatrix}$. After a cluster assignment step, what will $c^{(i)}$ be?  

* $c^{(i)} = 2$  
* $c^{(i)}$  is not assigned
* $c^{(i)} = 1$  
* $c^{(i)} = 3$  

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 计算$x^i$与每个$c^i$的距离=$||x^{(i)} - \mu_{c^{(i)}}||^2$,取最小的</font> **   
** <font color=red> 与$\mu_1$的矩离=$[-2-(1)]^2+[1-2]^2=9+1=10$   </font> **    
** <font color=red> 与$\mu_2$的矩离=$[-2-(-3)]^2+[1-0]^2=1+1=2$   </font> **   
** <font color=red> 与$\mu_3$的矩离=$[-2-(4)]^2+[1-2]^2=36+1=37$   </font> **
** <font color=red>  所以与$\mu_2$的矩离最小  </font> **

--- 
### 第 3 题
K-means is an iterative algorithm, and two of the following steps are repeatedly carried out in its inner-loop. Which two?

* Move the cluster centroids, where the centroids $\mu_k$ are updated.  
* The cluster assignment step, where the parameters $c^{(i)}$ are updated.    
* Move each cluster centroid $\mu_k$, by setting it to be equal to the closest training example $x^{(i)}$  
* The cluster centroid assignment step, where each cluster centroid $\mu_i$ is assigned (by setting $c^{(i)}$) to the closest training example $x^{(i)}$.  

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 2 4 --> 这个答案不正确</font> ** 
 
* Move the cluster centroids, where the centroids $\mu_k$ are updated.  
* The cluster centroid assignment step, where each cluster centroid $\mu_i$ is assigned (by setting $c^{(i)}$) to the closest training example $x^{(i)}$.  
* The cluster assignment step, where the parameters $c^{(i)}$ are updated.  
* Move each cluster centroid $\mu_k$, by setting it to be equal to the closest training example $x^{(i)}$   
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 3  正确</font> ** 

---
### 第 4 题
Suppose you have an unlabeled dataset $\{x^{(1)}, \ldots,  x^{(m)}\}$. You run K-means with 50 different random  
initializations, and obtain 50 different clusterings of the data. What is the recommended way for choosing which one of  
these 50 clusterings to use?  

* The only way to do so is if we also have labels $y^{(i)}$ for our data.  
* For each of the clusterings, compute $\frac{1}{m} \sum_{i=1}^m{ ||x^{(i)} - \mu_{c^{(i)}}||^2}$, and pick the one that minimizes this.  
* The answer is ambiguous, and there is no good way of choosing.  
* Always pick the final (50th) clustering found, since by that time it is more likely to have converged to a good solution.    

** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 </font> **  
** <font color=red> 代价函数最小的才行 </font> **  

---
## 第 5 题
Which of the following statements are true? Select all that apply.  

* If we are worried about K-means getting stuck in bad local optima, one way to ameliorate (reduce) this problem is if we try using multiple random initializations.  
* The standard way of initializing K-means is setting μ1=⋯=μk to be equal to a vector of zeros.  
* Since K-Means is an unsupervised learning algorithm, it cannot overfit the data, and thus it is always better to have as large a number of clusters as is computationally feasible.  
* For some datasets, the "right" or "correct" value of K (the number of clusters) can be ambiguous, and hard even for a human expert looking carefully at the data to decide.  

** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 1 4 </font> **  
** <font color=red>选项1: </font> **  

 * K-Means will always give the same results regardless of the initialization of the centroids.  
 * A good way to initialize K-means is to select K (distinct) examples from the training set and set the cluster centroids equal to these selected examples.  
 * On every iteration of K-means, the cost function $J(c^{(1)}, \ldots, c^{(m)}, \mu_1, \ldots,\mu_k)$ (the distortion function) should either stay the same or decrease; in particular, it should not increase.  
 * Once an example has been assigned to a particular centroid, it will never be reassigned to another different centroid.  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 3 </font> **  
** <font color=red>选项1: 跟初始值有很大关系. 不正确 </font> **  
** <font color=red>选项2:  正确 </font> **  
** <font color=red>选项3:  正确 </font> ** 