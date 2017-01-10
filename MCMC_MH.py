#-*- coding:utf8 -*-
__date__ = "01/08/2017"
__author__ = "KeithYin"
import  numpy as np
import matplotlib.pyplot as plt
def gaussian(x, mean, variance):
    res = 1/((np.sqrt(2*np.pi))*variance) * np.exp(-np.square(x-mean)/(2*np.square(variance)))
    return res

def multi_gaussian(x):
    res = 0.3*gaussian(x,0,2)+0.7*gaussian(x,20,3)
    return res
def accept(sampled, value):
#calculate the acception rate
    val1 = (multi_gaussian(value) * gaussian(sampled[-1], value, 20))
    val2 = (multi_gaussian(sampled[-1]) * gaussian(value, sampled[-1], 20))
    thresh_hold = val1/val2
    return np.min([1,thresh_hold])

def MCMC():
    sampled = [1.0]
    for i in range(100000):
        value = np.random.normal(sampled[-1],10)# sample a new sample
        u = np.random.uniform(0,1) # sample the threshold
        if u < accept(sampled, value):
            sampled.append(value)
        else:
            sampled.append(sampled[-1])
    return sampled

def main():
    sampled = MCMC()
    print(len(sampled))
    plt.hist(sampled, bins=100, normed=True)
    plt.show()

if __name__ == "__main__":
    main()



