def reg(x, y):
	xMean = sum(x)/len(x)
	yMean = sum(y)/len(y)
	a = sum([(x[i] - xMean)*(y[i] - yMean) for i in range(len(x))]) / sum([(x[i] - xMean)**2 for i in range(len(x))])
	b = yMean - a * xMean
	return a, b

x = list(map(float, input('Enter x Values: ').split()))
x = list(map(float, input('Enter y Values: ').split()))

a, b = reg(x, y)

print(f'y = {"{0:.2f}".format(a)}x + {"{0:.2f}".format(b)}')

print(a*float(input('Predict: '))+b)
