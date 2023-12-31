
from __future__ import print_function
import tensorflow as tf


def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size])) #隨機變量
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1) #列表 ，初始值不為零
    Wx_plus_b = tf.matmul(inputs, Weights) + biases #沒有被激活
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs