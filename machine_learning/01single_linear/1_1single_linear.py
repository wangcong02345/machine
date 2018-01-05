#coding:utf-8
__author__ = 'wangcong'
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 加载数据: 每行两个值,一个是x1,一个是Y
# 6.1101,17.592
# 5.5277,9.1302
# 8.5186,13.662
def loadDataSet():
    # 将数据从文档中加载进内存
    path = './ex1data1.txt'
    data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
    # 插入一列全为1的x0
    data.insert(0, 'Ones', 1)
    # 将数据分割为x 与 y, 其中x包含两项(x0,x1)
    cols = data.shape[1]
    x = data.iloc[:, 0:cols - 1]  # x是所有行，去掉最后一列
    y = data.iloc[:, cols - 1:cols]  # y是所有行，最后一列
    # 将x与y都转为matrix 方便计算
    x = np.matrix(x.values)
    y = np.matrix(y.values)
    return data, x, y

# 计算损失函数
def computeCost(X, y, theta):
    inner = np.power(((X * theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

# 批量梯度下降
def gradientDescent22(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))
        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost

# 批量梯度下降
def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    for i in range(iters):
        error = (X * theta.T) - y
        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))
        theta = temp
    return theta

# 画出结果
def plot_data(data, g):
    x = np.linspace(data.Population.min(), data.Population.max(), 100)
    f = g[0, 0] + (g[0, 1] * x)
    fig, ax = plt.subplots(figsize=(12,8))
    ax.plot(x, f, 'r', label='Prediction')
    ax.scatter(data.Population, data.Profit, label='Traning Data')
    ax.legend(loc=2)
    ax.set_xlabel('Population')
    ax.set_ylabel('Profit')
    ax.set_title('Predicted Profit vs. Population Size')
    plt.show()

if __name__ == '__main__':
    (data,x,y) = loadDataSet()
    theta = np.matrix(np.array([0,0]))
    print x.shape,  y.shape, theta.shape, theta.T.shape
    #print("x=%s" % x)
    #print("y=%s" % y)

    alpha = 0.01
    iters = 1000
    #(theta,cost) = gradientDescent(x,y,theta,alpha,iters)
    theta  = gradientDescent(x, y, theta, alpha, iters)
    print theta
    #print cost[-1]
    plot_data(data, theta)