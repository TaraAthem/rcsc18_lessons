import glob
import numpy as np
import matplotlib.pyplot as plt

import analysistools

filenames = sorted(glob.glob('../03-fundamentals-of-python/inflammation*.csv'))

for f in filenames[:3]:
	print(f)
	analysistools.analyse(f)
	analysistools.detect_problems(f)



	
	
