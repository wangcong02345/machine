# Week 2 | 2_OctaveMatlab Tutorial

### 第 1 题
Suppose I first execute the following in Octave/Matlab:  
A = [1 2; 3 4; 5 6];  
B = [1 2 3; 4 5 6];  
Which of the following are then valid commands?   
Check all that apply. (Hint: A' denotes the transpose of A.)   

* C = A' + B;  
* C = B * A;  
* C = A + B;  
* C = B' * A;  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: A B  
 A是3x2 B 2x3  
选项1: A的转置是2x3, B是2x3,行列相同可以相加. 正确  
选项2: A是3x2, B是2x3,相乘后是3x3的矩阵.  正确
选项3: A是3x2, B是2x3,行列不同不能相加. 不正确  
选项4: B的转置是3x2, A是3x2,无法相乘.  不正确 </font> **

---
### 第 2 题
Let $A = \begin{bmatrix} 16 & 2 & 3 & 13 \\ 5 & 11 & 10 & 8 \\ 9 & 7 & 6 & 12 \\ 4 & 14 & 15 & 1 \end{bmatrix}$  
Which of the following indexing expressions gives $B = \begin{bmatrix} 16 & 2 \\ 5 & 11 \\ 9 & 7 \\ 4 & 14 \end{bmatrix}$? Check all that apply.

* B = A(:, 1:2);
* B = A(1:4, 1:2);
* B = A(:, 0:2);
* B = A(0:4, 0:2);  
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: AB,取A的前两列就是B  
A(:, 1:2)取所有列是A(1:4, 1:2)的省略写法 </font> ** 
   
--- 
### 第 3 题
Let A be a 10x10 matrix andx be a 10-element vector. Your friend wants to compute the product Ax and writes the following code: 
```python
v = zeros(10, 1);
for i = 1:10
  for j = 1:10
    v(i) = v(i) + A(i, j) * x(j);
  end
end
```
How would you vectorize this code to run without any for loops? Check all that apply.  

* v = A * x;
* v = Ax;
* v = x' * A;
* v = sum (A * x);  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案:A $A_00*x_0+A_01*x_1+A_02*x_2+....$就是A*x</font> **  

---
### 第 4 题
Say you have two column vectors v and w, each with 7 elements (i.e., they have dimensions 7x1). Consider the following code:   
```python
z = 0;
for i = 1:7
  z = z + v(i) * w(i)
end
```
Which of the following vectorizations correctly compute z? Check all that apply.

* z = sum (v .\* w);
* z = w' \* v;
* z = v \* w';
* z = w \* v';
 
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 1  
v是7x1 w是7x1, 上述代码的最终的结果是一个数值  
选项1: v=[1 2 3] w=[4 5 6] v.*w= [4   10   18],再对[4 10 18]求和. 正确  
选项2: w转置是1x7,v是7x1, 则v*w是一个数值. 正确  
选项3: v是7x1, w转置是1x7,则v*w是7x7的矩阵. 不正确  
选项4: w是7x1, v转置是1x7, 则v*w是7x7的矩阵. 不正确  
</font> **  

---
## 第 5 题
In Octave/Matlab, many functions work on single numbers, vectors, and matrices. For example, the sin function when applied to a matrix will return a new matrix with the sin of each element. But you have to be careful, as certain functions have different behavior. Suppose you have an 7x7 matrix X. You want to compute the log of every element, the square of every element, add 1 to every element, and divide every element by 4. You will store the results in four matrices, A,B,C,D. One way to do so is the following code:
```python
for i = 1:7
  for j = 1:7
    A(i, j) = log(X(i, j));
    B(i, j) = X(i, j) ^ 2;
    C(i, j) = X(i, j) + 1;
    D(i, j) = X(i, j) / 4;
  end
end
```

* C = X + 1;
* D = X / 4;
* A = log (X); 
* B = X ^ 2;  
Which of the following correctly compute A,B,C, or D? Check all that apply.  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案:  A B C  
选项4:  X ^ 2= X*X是矩阵相乘,向量两两相乘的结果  
但是程序中的 $(X_i)_j$ ^ 2,是对$(X_i)_j$ 是对单个数值求平方再写成矩阵,两者意义是不一样的  
正确的写法是 B = X .* X  
 </font> **   

