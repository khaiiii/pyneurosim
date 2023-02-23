import Param
import numpy as np
import random

class Array:
    def __init__(self, x, y, arrayrowsize, voltage, conductance):
        self.x = x
        self.y = y
        self.arrayrowsize = arrayrowsize
        self.voltage = voltage
        self.conductance = conductance

    ArrayIH = np.full((Param.nHide1, Param.nInput), 3.0769e-9 + (3.8462e-8 - 3.0769e-9) * random.random())
    ArrayHH = np.full((Param.nHide2, Param.nHide1), 3.0769e-9 + (3.8462e-8 - 3.0769e-9) * random.random())
    ArrayHO = np.full((Param.nOutput, Param.nHide2), 3.0769e-9 + (3.8462e-8 - 3.0769e-9) * random.random())

    array = [ArrayIH, ArrayHH, ArrayHO]

class Input:
    Input = np.zeros((60000, 28*28))
    dInput = np.zeros((60000, 28*28))

Output = []
class Output:
    Output = np.zeros((Param.laynum, Param.layer[0]), dtype='int16')

RefCol = []
class RefCol:
    RefCol = np.full((Param.laynum, Param.layer[0]), (3.0769e-9 + 3.8462e-8)/2)


class Cell(Array):
    def ReadCell(self):
        arraywirewidth = 100 * 1e-9
        unitR = 2.73e-8 * (100 * 2) / (100 * (100 * 2.3) * 1e-9)
        wireResistance = (2.73e-8 / (arraywirewidth * arraywirewidth * 2.30)) * (arraywirewidth * 2)
        totalwireResistance = unitR * (self.x + (self.arrayrowsize - self.y)) + Param.accessresistance
        current = self.voltage / (1 / self.conductance + totalwireResistance)

        return current