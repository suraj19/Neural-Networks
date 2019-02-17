'''Date: 16-01-19
Author: Suraj Kumar
XOR Gate operations using the Mcculloch-Pitts Neuron Model'''
def activation_function_xor(yin):
    if yin >= 1:
        return 1
    else:
        return 0
def activation_function_zin(zin):
    if zin >= 1:
        return 1
    else:
        return 0
X1 = [0,0,1,1]
X2 = [0,1,0,1]
w1 = 1
w2 = -1
result1 = []
result2 = []
summ = []
for i,j in zip(X1,X2):
    zin1 = w1*i + w2*j
    summ.append(zin1)
    result1.append(activation_function_zin(zin1))
for i,j in zip(X1,X2):
    zin2 = w2*i + w1*j

    result2.append(activation_function_zin(zin2))
print('The output of 1st Neuron: ',result1)
print('The output of 2nd Neuron: ',result2)
for i,j in zip(result1,result2):
    zin2 = i + j
    #result.append(activation_function_xor(zin2))
    print('The output for a given input {} and {} using XOR Gate:'.format(i,j),activation_function_xor(zin2))
