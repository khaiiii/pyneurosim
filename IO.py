import tensorflow
import math
import numpy as np
import Array

def readMNISTdataset():
    mnist = tensorflow.keras.datasets.mnist
    (Input, Output), (testInput, testOutput) = mnist.load_data()


    #Input = Input/255.0
    testInput = testInput/255.0

    Input = Input.reshape(60000, 28*28)
    testInput = testInput.reshape(10000, 28*28)

    Array.Input.Input = Input
