import tensorflow
import math
import numpy as np

def readMNISTdataset():
    mnist = tensorflow.keras.datasets.mnist
    (Input, Output), (testInput, testOutput) = mnist.load_data()

    Input = np.around(Input/255.0)
    testInput = np.around(testInput/255.0)


    Input = Input.reshape(60000, 28*28)
    testInput = testInput.reshape(10000, 28*28)

    
