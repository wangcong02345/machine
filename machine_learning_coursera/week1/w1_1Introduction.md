# Week 1 | 1_Introduction
### 第 1 题
A computer program is said to learn from experience E with respect to some task T and some performance measure P if its
performance on T, as measured by P, improves with experience E.
Suppose we feed a learning algorithm a lot of historical weather
data, and have it learn to predict weather. What would be a
reasonable choice for P?  

* The process of the algorithm examining a large amount of historical weather data.
* None of these.
* The probability of it correctly predicting a future date's weather.
* The weather prediction task.  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;解析: 一个程序被认为能从经验 E 中学习，解决任务 T，达到性能度量值P
 第1个选项是E, 第3个选项是P, 第4个选项是E</font> **
---
### 第 2 题
Suppose you are working on weather prediction, and use a
learning algorithm to predict tomorrow's temperature (in degrees Centigrade/Fahrenheit).
Would you treat this as a classification or a regression problem?  
 
 * Classification  
 * Regression  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;解析: 如果预测的结果为连续的值，是回归问题; 如为离散的值，是分类问题  
    题目中的温度是连续的值,所以是回归 </font> **

---
### 第 3 题 
Suppose you are working on stock market prediction, Typically 
tens of millions of shares of Microsoft stock are traded 
(i.e., bought/sold) each day. You would like to predict the 
number of Microsoft shares that will be traded tomorrow. 
Would you treat this as a classification or a regression problem? 

* Classification
* Regression  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;解析: 如果预测的结果为连续的值，是回归问题; 如为离散的值，是分类问题  
    题目中的number也是连续的值,所以也是回归 </font> **

---
### 第 4 题 
Some of the problems below are best addressed using a supervised learning algorithm, and the others with an unsupervised learning algorithm. Which of the following would you apply supervised learning to? (Select all that apply.) In each case, assume some appropriate dataset is available for your algorithm to learn from.

* Take a collection of 1000 essays written on the US Economy, and find a way to automatically group these essays into a small number of groups of essays that are somehow "similar" or "related".
* Given historical data of children's ages and heights, predict children's height as a function of their age.
* Given 50 articles written by male authors, and 50 articles written by female authors, learn to predict the gender of a new manuscript's author (when the identity of this author is unknown).
* Examine a large collection of emails that are known to be spam email, to discover if there are sub-types of spam mail.  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;解析:区分监督与非监督学习,关键是看有没有标准  
选项1: 给定1000篇文章，自动把这些文章分为相似的还是相关的.没有给出分类标准属于非监督学习    
选项2: 给定儿童的身高与年年龄的历史数据,去预测一个儿童在某岁时的身高,是监督学习  
选项3: 给定50个男作者与50个女作者的文章,再给一个文章去预测是男作者还是女作者,是监督学习  
选项4: 给定一堆垃圾邮件,然后去发现垃圾邮件的子类型,没有分类标准所以是非监督学习   
以上2的标准就是这个儿童的身高, 3的标准就是作者的性别,所以是监督学习  
1与4找不到标准,所以是非监督学习  </font> **

---
### 第 5 题 
Which of these is a reasonable definition of machine learning?

* Machine learning learns from labeled data.
* Machine learning is the science of programming computers.
* Machine learning is the field of allowing robots to act intelligently.
* Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.  
**<font color=red>&nbsp;&nbsp;&nbsp;&nbsp;解析: 机器学习是给计算机一种不需要明确程序命令可以自学习的能力,所以选D。  
三短一长选最长!!! </font> **