import Param
import numpy as np
import random

class Array:
    def ReadCell(x, y, arrayrowsize, voltage, conductance):
        arraywirewidth = 100 * 1e-9 #nm

        wireResistance = (2.73e-8 / (arraywirewidth * arraywirewidth * 2.30)) * (arraywirewidth * 2)
        totalwireResistance = (x - 1 + (arrayrowsize - y)) * wireResistance + 15e3 #Acces Resistance
        current = voltage / (1 / conductance + totalwireResistance)

        return current  

class ArrayIH(Array):
    ArrayIH = np.random.rand(Param.nInput, Param.nHide1) #conductance
    arrayrowsize = Param.nInput 
    

class ArrayHH(Array):
    ArrayHH = np.random.rand(Param.nHide1, Param.nHide2)
    arrayrowsize = Param.nHide1

class ArrayHO(Array):
    ArrayHO = np.random.rand(Param.nHide2, Param.nOutput)
    arrayrowsize = Param.nHide2

class Input:
    Input = np.zeros((60000, 28*28))
    dInput = np.zeros((60000, 28*28))


Output = []
class Output:
    Output = np.zeros((Param.laynum, Param.layer[0]))


