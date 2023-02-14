import random
import numpy as np
import Param

def Train(epochs):
    for t in epochs:
        i = random(1, 60000) #randomize sampe

        outN1 = np.zeros(Param.nHide1)
        a1 = np.zeros(Param.nHide1)

        

        
