import random
import numpy as np
import Param
import Array
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

IV = 1.0 / (3.8462e-8 - 3.0769e-9) / (2 * 0.5)

def Train(Input):
    epochs = 1
    for t in range(0, epochs):
        i = random.randint(0, 60000)
        Output = Array.Output.Output

        for n in range(0, Param.layer[0]):
            Output[0][n] = round(Input[i][n] / 256 * math.pow(2, Param.numBit))
            
        # hardware FeedForward
        if(Param.useHardwareInFF):
            for layer in range(0, Param.laynum - 1): # 4 layer(I, H1, H2, O) 0 1 2 
                BitSlice = np.zeros((Param.numBit, Param.layer[0]))

                for n in range(0, Param.layer[layer]): # Bit Slicing numBit is 1
                    for t in range(0, Param.numBit):
                        if((Output[layer][n] >> t) > 0):
                            BitSlice[t][n] = Param.readVoltage

                totalcurrent = np.zeros(Param.layer[layer+1])
                for n in range(0, Param.numBit): # current
                    Isum = np.zeros(Param.layer[layer+1])
                    IsumCol = 0
                    
                    for x in range(0, Param.layer[layer+1]):
                        temp2 = Array.Array(x, Param.layer[layer] - 1, Param.layer[layer] - 1, BitSlice[n][x], Array.RefCol.RefCol[layer][x])
                        IsumCol = temp2.ReadCell()                   
                        for y in range(0, Param.layer[layer]):
                            temp = Array.Array(x, y, Param.layer[layer] - 1, BitSlice[n][y], Array.ArrayIH.ArrayIH[x][y])
                            Isum[x] += temp.ReadCell()

                        totalcurrent[x] += (Isum[x] - IsumCol) / math.pow(2, Param.numBit - n - 1)

                    for x in range(0, Param.layer[layer+1]):
                        Output[layer+1][x] = sigmoid(totalcurrent[x])
            
        
        # hardware BackPropagation
        #if(Param.useHardwareInBP):
            
