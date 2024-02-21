
import numpy as np
class NeuralNetwork:
  def __init__(self,W1,W2):
       self.W1=W1
       self.W2=W2
  def sigmoid(self,X):
     return 1/(1+np.exp(-X))
  def dense(self,a,W,activation):
       a_next=np.matmul(W.T,a)
       return activation(a_next),a_next
  def sequential(self,X,W1,W2):
    a1,Z1=self.dense(X,W1,self.sigmoid)
    a2,Z2=self.dense(a1,W2,self.sigmoid)
    return a1,Z1,W1,a2,Z2,W2
  def predict(self,k,W1,W2):
    a1,Z1,W1,a2,Z2,W2=self.sequential(k,W1,W2)
    output=[]
    for i in a2.T:
       if i>=.5:
          output.append(1)
       else:
           output.append(0)
    return np.array(output)
  











