# linearRegression
Returns line of best fit given data points in the form (x, y)

![image](https://user-images.githubusercontent.com/62809012/142138508-8da07572-ec56-4c0a-a4c8-56c3391b87e6.png)

Pocket Linear Regression:
```python
def reg(x, y): return sum([(x[i] - sum(x)/len(x))*(y[i] - sum(y)/len(y)) for i in range(len(x))]) / sum([(x[i] - sum(x)/len(x))**2 for i in range(len(x))]), yMean - a * xMean
```
