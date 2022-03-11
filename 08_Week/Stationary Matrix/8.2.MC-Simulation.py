import numpy as np
import pandas as pd
from random import seed
from random import random
import matplotlib.pyplot as plt
from pyparsing import commonHTMLEntity
import imageio


transition_probability_matrix = np.array([[0.2, 0.7, 0.1],
              [0.9, 0.0, 0.1],
              [0.2, 0.8, 0.0]])
state=np.array([[1.0, 0.0, 0.0]])
stateHist=state
dfStateHist=pd.DataFrame(state)
distr_hist = [[0,0,0]]

images = []

for x in range(21):
  state=np.dot(state,transition_probability_matrix)
  #print(state)
  stateHist=np.append(stateHist,state,axis=0)
  dfDistrHist = pd.DataFrame(stateHist)
  dfDistrHist.plot()
  plt.axis((0, 20, 0, 1))
  plt.savefig('plot_'+str(x)+'.png', dpi=300, format='png', facecolor='white')
  plt.close()

  
  filename = 'plot_{}.png'.format(x)
  images.append(imageio.imread(filename))
  imageio.mimsave('MC-Simulation.gif', images, fps=2)
#plt.show()
