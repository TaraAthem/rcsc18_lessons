import numpy as np
import matplotlib.pyplot as plt
import random

def pi_est(n):

	x=[random.random() for _ in range(0, n)]
	y=[random.random() for _ in range(0, n)]

	counter1= 0
	counter2= 0

	r1= np.sqrt(np.array(x)**2 + np.array(y)**2)
	#print(len(x),len(y),len(r1))
	counter1= sum(float(i) <= 1 for i in r1)
	counter2=len(r1)

	pi_est= 4*counter1/counter2

	print(pi_est)
	
	xc=np.arange(0, 1.1, 0.01)
	yc=np.sqrt(1- np.array(xc)**2)

	#print(np.array(x)[r1 < 1])
	plt.scatter(np.array(x)[r1 < 1.],np.array(y)[r1 < 1.], marker=".", color='b')
	plt.scatter(np.array(x)[r1 > 1.],np.array(y)[r1 > 1.], marker=".", color='r')
	plt.plot(xc,yc, 'k--')
	plt.title('Approximating Pi')
	plt.axis([0, 1, 0, 1])
	plt.show()

pi_est(50)
#OLD CODE
#for i in range(9999):
#	r1=np.sqrt(x[i]**2 + y[i]**2)
#	if r1 < 1:
#		counter1= counter1 + 1
#	counter2=counter2 +1
#