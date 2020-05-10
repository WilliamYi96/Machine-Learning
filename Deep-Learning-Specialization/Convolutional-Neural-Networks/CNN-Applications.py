import math
import numpy as np 
import h5py
import matplotlib.pyplot as plt 
from PIL import Image
from scipy import ndimage
import tensorflow as tf 
from tensorflow.python.framework import ops
from cnn_utils import *

np.random.seed(1)

# Loading the data (signs)
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()

# Example of a picture
index = 5
plt.imshow(X_train_orig[index])
# print(Y_train_orig.shape, np.squeeze(Y_train_orig).shape)
print('y = ' + str(np.squeeze(Y_train_orig)[index]))
# print('y = ' + str(np.squeeze(Y_train_orig[:,index])))
plt.show()

X_train = X_train_orig / 255.
X_test = X_test_orig / 255. 
Y_train = convert_to_one_hot(Y_train_orig, 6).T 
Y_test = convert_to_one_hot(Y_test_orig, 6).T
print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))
conv_layers = {}

def create_placeholders(n_H0, n_W0, n_C0, n_y):
    '''
    Creates the placeholders for the tensorflow session.

    Arguments:
    n_H0 -- scalar, height of an input image
    n_W0 -- scalar, width of an input image
    n_C0 -- scalar, number of channels of the input
    n_y -- scalar, number of classes

    Returns:
    X -- placeholder for the data input, of shape [None, n_H0, n_W0, n_C0] and dtype 'float'
    Y -- placeholder for the input labels, of shape [None, n_y] and dtype 'float'
    '''

    X = tf.placeholder(shape=[None, n_H0, n_W0, n_C0], dtype=tf.float32)
    Y = tf.placeholder(shape=[None, n_y], dtype=tf.float32)

    return X, Y

X, Y = create_placeholders(64, 64, 3, 6)
print('X = {}'.format(X))
print('Y = {}'.format(Y))

# Continue from Initialize parameters.
# https://walzqyuibvvdjprisbmedy.coursera-apps.org/notebooks/week1/Convolution_model_Application_v1a.ipynb#1.2---Initialize-parameters