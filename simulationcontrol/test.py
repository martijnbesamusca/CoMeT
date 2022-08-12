
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

for y in range(100):
    xs = np.linspace(0, 100, 10)
    ys = (xs+100/(1+y))
    plt.plot(xs, ys)
    