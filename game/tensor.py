'''
Created on Dec 31, 2018

@author:  cpendery, wmuller
'''


import tensorflow as tf
import numpy as np

#7 params
#{distance to ob, height of ob, width of ob, bird height, speed, player y pos, gap between obs}
#3 lables
#0 = stay, 1 = jump, 2 = duck
input = np.array([[1,1,1,1,1,1,1],[2,2,2,2,2,2,2]], np.int32)
labels = np.array([0,2])

dataset = tf.data.Dataset.from_tensor_slices((input,labels))
