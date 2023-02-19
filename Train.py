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
            for layer in range(0, Param.laynum - 1): # 4 layer(I, H1, H2, O) 0 1 2 -> 3times
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
                            temp = Array.Array(x, y, Param.layer[layer] - 1, BitSlice[n][y], Array.Array.array[layer][x][y])
                            Isum[x] += temp.ReadCell()

                        totalcurrent[x] += (Isum[x] - IsumCol) / math.pow(2, Param.numBit - n - 1)

                    for x in range(0, Param.layer[layer+1]):
                        Output[layer+1][x] = sigmoid(totalcurrent[x])
            
        
        # hardware BackPropagation
        # WU in pulse system
        if(Param.usePulseInWU):
            for layer in range(0, Param.laynum - 1):
                maxNumLevelLTP = 97
                maxNumLevelLTD = 100

                probConstLTP = math.sqrt((Param.learningRate / pow(2, int(epochs/10))) * maxNumLevelLTP / (Param.StreamLength * 2))
                probConstLTD = math.sqrt((Param.learningRate / pow(2, int(epochs/10))) * maxNumLevelLTD / (Param.StreamLength * 2))

                InputPulseTrain = []
                DeltaPulseTrain = []
                for n in Param.layer[layer]:
                    ipLTP = abs(Output[layer][n] / 256 * probConstLTP)
                    ipLTD = abs(Output[layer][n] / 256 * probConstLTD)

                    InputPulseLTP = np.random.binomial(1, ipLTP, Param.StreamLength)
                    InputPulseLTD = np.random.binomial(1, ipLTD, Param.StreamLength)
                    InputPulseTrain = np.concatenate((InputPulseLTP, InputPulseLTD))

                for n in Param.layer[layer+1]:
                    dpLTP = abs(Output[layer+1][n] / 256 * probConstLTP)
                    dpLTD = abs(Output[layer+1][n] / 256 * probConstLTD)

                    DeltaPulseLTP = np.random.binomial(1, dpLTP, Param.StreamLength)
                    DeltaPulseLTD = np.random.binomial(1, dpLTD, Param.StreamLength)
                    DeltaPulseTrain = np.concatenate((DeltaPulseLTP, DeltaPulseLTD))

                