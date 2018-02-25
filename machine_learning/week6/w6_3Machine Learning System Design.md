# Week6_3Machine Learning System Design
### 第 1 题
You are working on a spam classification system using regularized logistic regression. "Spam" is a positive class (y = 1) and "not spam" is the negative class (y = 0). You have trained your classifier and there are m = 1000 examples in the cross-validation set. The chart of predicted class vs. actual class is:

|                       | Actual Class: 1    | Actual Class: 0 |
| ----------            | ---           | ---     |
| Predicted Class: 1    |  85           |  890   |
| Predicted Class: 0    |  15           |  10  |

For reference:

* Accuracy = (true positives + true negatives) / (total examples)
* Precision = (true positives) / (true positives + false positives)
* Recall = (true positives) / (true positives + false negatives)
* $F_1$ score = (2 * precision * recall) / (precision + recall)
What is the classifier's recall (as a value from 0 to 1)?    
Enter your answer in the box below.  
If necessary, provide at least two values after the decimal point.

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 0.85 </font> **  
** <font color=red>  * 预测正确的数量是: 85+10=95  预测错误的是:890+15=905  </font> **  
** <font color=red>  * 查全率Recall = (true positives) / (true positives + false negatives) </font> **  
** <font color=red>  * true positives = 85   false negatives=15 </font> **  
** <font color=red>  * recall = 85/(85+15)=0.85 </font> **  

What is the classifier's accuracy (as a value from 0 to 1)?  

** <font color=red>  classifier's accuracy = (85+10)/1000=0.095 </font> ** 

---
### 第 2 题
Suppose a massive dataset is available for training a learning algorithm. Training on a lot of data is likely to give good performance when two of the following conditions hold true.  
Which are the two?  

* The features x contain sufficient information to predict y accurately. (For example, one  
way to verify this is if a human expert on the domain can confidently predict y when given only x).
* We train a learning algorithm with a small number of parameters (that is thus unlikely to overfit).
* We train a learning algorithm with a large number of parameters (that is able to learn/represent fairly complex functions).
* We train a model that does not use regularization.

<font color=red>** &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 3   ** </font>  
<font color=red>** 以下哪两种情况下, 当用更多的样本去训练时,会得出更好的结果. ** </font>   
<font color=red>** 选项1: 给专家一个x feature就可以准确的预测出y. 即所选的特征x含有足够的信息来准确预测y,这感觉是废话. 正确 **  </font>  
<font color=red>** 选项2: 只有少数参数的模型时会导致欠拟合,这时用更多的样本去训练也没有用.  不正确 **  </font>  
<font color=red>** 选项3: 当使用大量数参数的模型时会导致过拟合,这时用更多的样本去训练会使过拟合减轻.  正确  **  </font> 
<font color=red>** 选项4:使不使用正则化跟更多样本去训练没关系.   **  </font> 

* We train a learning algorithm with a small number of parameters (that is thus unlikely to overfit).
* When we are willing to include high order polynomial features of x (such as $x_2^1$, $x_2^2$, $x_1x_2$, etc.).
* The features x contain sufficient information to predict y accurately. (For example, one way to verify this is if a human expert on the domain can confidently predict y when given only x).
* We train a learning algorithm with a large number of parameters (that is able to learn/represent fairly complex functions).
<font color=red>** &nbsp;&nbsp;&nbsp;&nbsp;答案:  3 4   ** </font>  
<font color=red>** 以下哪两种情况下, 当用更多的样本去训练时,会得出更好的结果. ** </font>   
<font color=red>** 选项1: 只有少数参数的模型时会导致欠拟合,这时用更多的样本去训练也没有用.  不正确 **  </font>  
<font color=red>** 选项2: 如果features太少,多加入polynomial features 也不能够完全模拟出训练样本的特征. 就像预测房价,只用房子面积这一个特征,再加上面积1次方,2次方组成的polynomial,就算训练样本再多,也不能预测出正确的房价. 不正确  **  </font> 

--- 
### 第 3 题
Suppose you have trained a logistic regression classifier which is outputing $h_\theta(x)$.  
Currently, you predict 1 if $h_\theta(x) \geq \text{threshold}$,    
and predict 0 if $h_\theta(x) \geq \text{threshold}$, where currently the threshold is set to 0.5.   
Suppose you increase the threshold to 0.9. Which of the following are true? Check all that apply.  

* The classifier is likely to now have lower precision.
* The classifier is likely to have unchanged precision and recall, but lower accuracy. 
* The classifier is likely to have unchanged precision and recall, but higher accuracy. 
* The classifier is likely to now have lower recall.
 
** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 4 </font> **   
** <font color=red> threshold由0.5改变为0.9时,意思是:当$h_\theta(x) \geq 0.9$时为1,有90%的把握时才为1,为1的精确度大大提高 </font> **  
** <font color=red> 选项1: 为1的精确为大大提高. 不正确 </font> **  
** <font color=red> 选项2: precision大大提高,而不是unchange. 不正确 </font> **  
** <font color=red> 选项3: precision大大提高,而不是unchange. 不正确 </font> **  
** <font color=red> 选项4: recall为降低. 正确 </font> **  

Suppose you decrease the threshold to 0.3. Which of the following are true? Check all that apply. 

* The classifier is likely to now have higher recall.
* The classifier is likely to have unchanged precision and recall, but higher accuracy. 
* The classifier is likely to now have higher precision. 
* The classifier is likely to have unchanged precision and recall, but lower accuracy. 

** <font color=red> &nbsp;&nbsp;&nbsp;&nbsp;答案: 1 </font> **


---
### 第 4 题
Suppose you are working on a spam classifier, where spam emails are positive examples $(y=1)$ and non-spam emails are  
negative examples $(y=0)$. You have a training set of emails in which 99% of the emails are non-spam and the other 1% is spam.  
Which of the following statements are true? Check all that apply. 

* A good classifier should have both a high precision and high recall on the cross validation set.  
* If you always predict non-spam (output y=0), your classifier will have 99% accuracy on the training set, and it will likely perform similarly on the cross validation set.
* If you always predict non-spam (output y=0), your classifier will have an accuracy of 99%.
* If you always predict non-spam (output  y=0), your classifier will have 99% accuracy on the training set, but it will do much worse on the cross validation set because it has overfit the training data.   
 
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 3--> 这个答案是错的,但没有看出哪个选项错了,又做了一遍 </font> **  
** <font color=red> 对垃圾邮件进行分类, 为垃圾邮件时y=1; 不为垃圾邮件时y=0; 样本中99%的是非垃圾邮件,1%为垃圾邮件. </font> **  
** <font color=red> 选项1: 吴课程举的例子,当预测癌症是90%以上时才报告为得了癌症,虽然有high precision but low recall 但是我们认为这是一个好的算法. 满足需求才是最好的. 不正确 </font> **  
** <font color=red> 选项2: 全都报0,训练时有99%的成功率; 因为cross也是99%的非垃圾邮件,所以成功率也是99%. 正确 </font> **  
** <font color=red> 选项3: 全都报0,训练时有99%的成功率;正确 </font> **  
** <font color=red> 选项4: overfit是不对的是underfit. 不正确 </font> **  
** <font color=red> 再次确认,感觉这个题应该选 1 2 3 --> 没有难证过,错了请指出 </font> **  

* If you always predict spam (output y=1), your classifier will have a recall of 0% and precision of 99%.
* If you always predict non-spam (output y=0), your classifier will have a recall of 0%.
* If you always predict spam (output y=1), your classifier will have a recall of 100% and precision of 1%.
* If you always predict non-spam (output y=0), your classifier will have an accuracy of 99%.  
** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 3 4 --> 这个提交后是正确的</font> **  
** <font color=red> 对垃圾邮件进行分类, 为垃圾邮件时y=1; 不为垃圾邮件时y=0; 样本中99%的是非垃圾邮件,1%为垃圾邮件. </font> **  
** <font color=red> 选项1: 全报1,全都是垃圾邮件,精确度为1%,而不是99%. 不正确 </font> **  
** <font color=red> 选项2: 全都报0则true positives=0, recall=0,正确 </font> **  
** <font color=red> 选项3: 全报1,全都是垃圾邮件,精确度为1%,recall=100%;正确 </font> **  
** <font color=red> 选项4: 全报0,全都是非垃圾邮件,精确度99%. 正确 </font> **  

---
## 第 5 题
Which of the following statements are true? Check all that apply.  

*  It is a good idea to spend a lot of time collecting a large amount of data before building your first version of a  learning algorithm.  
*  On skewed datasets (e.g., when there are more positive examples than negative examples), accuracy is not a good measure of performance and you should instead use F1 score based on the precision and recall.  
* After training a logistic regression classifier, you must use 0.5 as your threshold for predicting whether an example is positive or negative.  
* Using a very large training set makes it unlikely for model to overfit the training data.  
* If your model is underfitting the  training set, then obtaining more data is likely to help.  

** <font color=red>&nbsp;&nbsp;&nbsp;&nbsp;答案: 2 4 </font> **  
** <font color=red> 对垃圾邮件进行分类, 为垃圾邮件时y=1; 不为垃圾邮件时y=0; 样本中99%的是非垃圾邮件,1%为垃圾邮件. </font> **  
** <font color=red> 选项1: 先迅速的写出一个模型,然后通过刚写出的这个模型来作为基准分析. 而不是一上来就去收集大量数据,因为都不知道收集大量样本数据是否会对模型有用. 不正确 </font> **  
** <font color=red> 选项2: 当出现skewed datasets时,预测全为0或全为1似乎会得到一个很高的准确率,但是recall会很低,通过F1来检验模型是否有效. 正确 </font> **  
** <font color=red> 选项3: threshold=0.5, 不是强制性的,完全可以人为设置这个threshold,例如想要90%的把握癌症才通知病人,防止病人过度担心.这时把threshold=0.9是完全可以的. 不正确 </font> **  
** <font color=red> 选项4: 当出现overfiting时,增多样本是可以解决. 正确 </font> **  
** <font color=red> 选项5: 当出现underfiting时,再多的样本数据也没有用.  不正确 </font> **  