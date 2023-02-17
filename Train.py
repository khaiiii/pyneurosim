import random
import numpy as np
import Param
import Array

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

IV = 1.0 / (3.8462e-8 - 3.0769e-9) / (2 * 0.5)

def Train(Input):
    epochs = 30
    for t in range(0, epochs):
        i = random.randint(0, 60000)
        Output = Array.Output.Output

        for n in range(0, Param.layer[0]):
            Output[0][n] = Input[i][n]

        # hardware FeedForward
        if(Param.useHardwareInFF):
            for layer in range(0, Param.laynum - 1): # 4 layer(I, H1, H2, O) 0 1 2 
                BitSlice = np.zeros((Param.numBit, Param.layer[0]))

                for n in range(0, Param.layer[layer]): # Bit Slicing numBit is 1
                    for t in range(0, Param.numBit):
                        if(Output[layer][n]):
                            BitSlice[t][n] = Param.readVoltage

                totalcurrent = np.zeros(Param.layer[layer+1])
                for n in range(0, Param.numBit): # current
                    Isum = np.zeros(Param.layer[layer+1])
                    IsumCol = 0
                    

                    for x in range(0, Param.layer[layer+1]):
                        IsumCol += Array.Array.ReadCell(x,Param.layer[layer], Param.layer[layer], BitSlice[n], Array.ArrayIH.ArrayIH[x][Param.layer[layer]])
                        for y in range(0, Param.layer[layer]):
                            Isum[x] += Array.Array.ReadCell(x, y, Param.layer[layer], BitSlice[n], Array.ArrayIH.ArrayIH[x][y])          
                        totalcurrent[x] += (Isum[x] - IsumCol) / pow(2, Param.numBit - n - 1)

                for n in range(0, Param.layer[layer+1]):
                    Output[layer+1][n] = sigmoid(totalcurrent * IV)