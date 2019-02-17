'''Date: 16-01-19
Author: Suraj Kumar
OR Gate operations using the Mcculloch-Pitts Neuron Model'''
def Neuron_input(i1,i2,w1,w2):
    y=i1*w1+i2*w2
    return y
def Activation_Function(y):
    result=y
    if y<1:
        return 0
    elif y>=1:
        return 1
'''input1=int(input())
input2=int(input())
weight1=np.random.randint(0,9)
weight2=np.random.randint(0,9)
#b=1
sigmodal_result=Neuron_input(input1,input2,weight1,weight2)
print(Activation_Function(sigmodal_result))'''
i1=[0,0,1,1]
i2=[0,1,0,1]
w1=1
w2=1
for i,j in zip(i1,i2):
    y=Neuron_input(i,j,w1,w2)
    print('The output for a given input {} and {} using OR Gate:'.format(i,j),Activation_Function(y))
