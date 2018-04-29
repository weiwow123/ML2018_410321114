from PIL import Image as img
import matplotlib.pyplot as plot
import numpy as np
import random as rd

E = img.open('/home/cos/IML_hw1/imgData/E.png')  #encryped img
I = img.open('/home/cos/IML_hw1/imgData/I.png')  #input img
K1 = img.open('/home/cos/IML_hw1/imgData/key1.png')  #encrypt key
K2 = img.open('/home/cos/IML_hw1/imgData/key2.png')  #encrypt key
EP = img.open('/home/cos/IML_hw1/imgData/Eprime.png')  #decrypt key

E_width = E.size[0]
E_height = E.size[1]
output_decrypt = img.new("L",(E_width,E_height))
output_encrypt = img.new("L",(E_width,E_height))

class GD():
    def __init__(self,eta=1e-10,epoch=10):
        self.eta = eta   #learning rate
        self.epoch = epoch
        self.w = [rd.random(),rd.random(),rd.random()]
        self.cost = []

    def train(self):
        print 'Training......'
        a = np.zeros((E_width,E_height),dtype='f')
        e = np.zeros((E_width,E_height),dtype='f')
        epoch = 0
        wk_1 = [0.0,0.0,0.0]  #w(k-1)
        while epoch<self.epoch and abs(wk_1[0]-self.w[0])+abs(wk_1[1]-self.w[1])+abs(wk_1[2]-self.w[2])>1e-10:
            print 'epoch: ',epoch+1,' W = [ ',self.w[0],' , ',self.w[1],' , ',self.w[2],' ]' 
            cost = 0
            for i in range(0,3):
                wk_1[i] = self.w[i]
                
            for i in range(0,E_width):
                for j in range(0,E_height):
                    a[i][j] = self.w[0]*K1.getpixel((i,j))+self.w[1]*K2.getpixel((i,j))+self.w[2]*I.getpixel((i,j))
                    e[i][j] = E.getpixel((i,j)) - a[i][j]
                    self.w[0] = self.w[0] + self.eta * e[i][j] * K1.getpixel((i,j))
                    self.w[1] = self.w[1] + self.eta * e[i][j] * K2.getpixel((i,j))
                    self.w[2] = self.w[2] + self.eta * e[i][j] * I.getpixel((i,j))
                    cost+=(e[i][j]**2)/2.0

            self.cost.append(cost/E_width*E_height)
            print 'cost: ',self.cost[epoch]
            epoch+=1

        return self

gd = GD(epoch=10,eta=1e-10).train()

#decrypt image Eprime
for i in range(0,E_width):
    for j in range(0,E_height):
        output_decrypt.putpixel((i,j),int(round((EP.getpixel((i,j))-gd.w[0]*K1.getpixel((i,j))-gd.w[1]*K2.getpixel((i,j)))/gd.w[2])))

output_decrypt.save('decrypted_EP1e-10_10.png')  #save decrypted image

plot.plot(range(1,len(gd.cost)+1),np.log10(gd.cost),marker='o')
plot.xlabel('Iterations')
plot.ylabel('log(sum_squared_error)')
plot.title('Adaline by Gradient Descent - LR=1e-10')
plot.show()
