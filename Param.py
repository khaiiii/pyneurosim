#layer
laynum = 4
nInput = 784
nHide1 = 256
nHide2 = 100
nOutput = 10
layer = [nInput, nHide1, nHide2, nOutput]

#useHardware
useHardwareInFF = True
useHardwareInBP = True
usePulseInWU = False

#numBit
numBit = 1 # signal is 1 or 0

#normal value
readVoltage = 0.5
learningRate = 0.01
maxconductance = 3.8462e-8
minconductance = 3.0769e-9
accessresistance = 15e3

#pulsesystem
StreamLength = 10