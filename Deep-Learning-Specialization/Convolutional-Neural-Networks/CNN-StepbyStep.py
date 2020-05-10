''' Implement convolutional neural network with CONV and POOL layer with numpy.
Motivated by https://walzqyuibvvdjprisbmedy.coursera-apps.org/notebooks/week1/Convolution_model_Step_by_Step_v2a.ipynb
Created by Kai Yi on March 1st, 2020
'''

import numpy as np 
import matplotlib.pyplot as plt
import h5py

# matplotlib inline
plt.rcParams['figure.figsize'] = (5.0, 4.0) # set default size of plots
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

np.random.seed(1) # keep all the random function calss consistent

def zero_pad(X, pad):
    '''
    Pad with zeros all images of the dataset X. 
    The padding is applied to the height and width of an image other than the example number and channel.

    Argument:
    X -- python numpy array of shape (m, n_H, n_W, n_C) reprensenting a batch of m images
    pad -- integer, amount of padding around each image on vertical and horizontal dimensions.

    Returns:
    X_pad -- padded image of shape (m, n_H + 2*pad, n_W + 2*pad, n_C)
    '''

    X_pad = np.pad(X, ((0,0), (pad,pad), (pad,pad), (0,0)), mode='constant', constant_values=(0,0))
    # (pad, pad) := (pad before, pad after), identical padding

    return X_pad

# test for zero_pad function
np.random.seed(1)
x = np.random.randn(4, 3, 3, 2)
x_pad = zero_pad(x, 2)
print('x.shape = \n', x.shape)
print('x_pad.shape = \n', x_pad.shape)
print('x[1,1] = \n', x[1,1])
print('x[1,1] = \n', x_pad[1,1])

fig, axarr = plt.subplots(1, 2)
axarr[0].set_title('x')
axarr[0].imshow(x[0,:,:,0], cmap='gray')
axarr[1].set_title('x_pad')
axarr[1].imshow(x_pad[0,:,:,0], cmap='gray')
plt.show()

def conv_single_step(a_slice_prev, W, b):
    '''
    Apply one filter defined by parameters W on a single sclie (a_slice_prev) of the output activation of the previous layer.

    Argument:
    a_slice_prev -- slice of input data of shape (f,f,n_C_prev)
    W -- Weight parameters contained in a window - matrix of shape (f,f,n_C_prev)
    b -- Bias parameters contained in a window - matrix of shape (1,1,1)

    Returns:
    Z -- a scalar value, the result of convolving the sliding window (W,b) on a slice x of the input data
    '''

    # Element-wise product between a_slice_prev and W.
    s = np.multiply(a_slice_prev, W)
    # Sum over all entries of the volume s.
    Z = np.sum(s)
    # Add bias b to Z. Cast b to a float() so than Z results in a scalar value.
    Z = Z + float(b)

    return Z

# test for conv_single_step
np.random.seed(1)
a_slice_prev = np.random.randn(4,4,3)
W = np.random.randn(4,4,3)
b = np.random.randn(1,1,1)

Z = conv_single_step(a_slice_prev, W, b)
print('Z = ', Z)

def conv_forward(A_prev, W, b, hparameters):
    '''
    Implements the forward propagation for a convolution function.

    Arguments:
    A_prev -- Output activations of the previous layer, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    W -- Weights, numpy array of shape (f, f, n_C_prev, n_C)
    b -- Biases, numpy array of shape (1, 1, 1, n_C)
    hparameters -- python dictionary containing 'stride' and 'pad'

    Returns:
    Z -- conv output, numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache of values needed for the conv_backward() function
    '''

    # Retrieve dimensions from A_prev's shape
    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    # Retrive dimensions from W's shape
    (f, f, n_C_prev, n_C) = W.shape
    # Retrive information from ''hparameters''
    stride, pad = hparameters['stride'], hparameters['pad']
    
    # Compute the dimensions of the CONV output volume
    n_H = int((n_H_prev - f + 2*pad) / stride + 1)
    n_W = int((n_W_prev - f + 2*pad) / stride + 1)
    # Initialize the output volume Z with zeros
    Z = np.zeros([m, n_H, n_W, n_C])
    # Create A_prev pad by padding A_prev
    A_prev_pad = zero_pad(A_prev, pad)

    for i in range(m):
        a_prev_pad = A_prev_pad[i]
        for h in range(n_H):
            vert_start = h * stride
            vert_end = vert_start + f 
            for w in range(n_W):
                horiz_start = w * stride
                horiz_end = horiz_start + f 
                for c in range(n_C):
                    a_slice_prev = a_prev_pad[vert_start:vert_end, horiz_start:horiz_end, :]
                    Z[i, h, w, c] = conv_single_step(a_slice_prev, W[:,:,:,c], b[:,:,:,c])
    assert(Z.shape == (m, n_H, n_W, n_C))

    cache = (A_prev, W, b, hparameters)

    return Z, cache

# test for conv_forward
np.random.seed(1)
A_prev = np.random.randn(10,5,7,4)
W = np.random.randn(3,3,4,8)
b = np.random.randn(1,1,1,8)
hparameters = {'pad' : 1,
                'stride' : 2}
Z, cache_conv = conv_forward(A_prev, W, b, hparameters)
print("Z's mean =\n", np.mean(Z))
print("Z[3,2,1] =\n", Z[3,2,1])
print("cache_conv[0][1][2][3] =\n", cache_conv[0][1][2][3])

def pool_forward(A_prev, hparameters, mode='max'):
    '''
    Implements the forward pass of the pooling layer

    Arguments:
    A_prev -- Input data, numpy array of shape (m, n_H_prev, n_W_prev, n_C_prev)
    hparameters -- python dictionary containing 'f' and 'stride'
    mode -- the pooling mode you would like to use, 'max' or 'average'

    Returns:
    A -- output of the pool layer, a numpy array of shape (m, n_H, n_W, n_C)
    cache -- cache used in the backward pass of the pooling layer, contains the input and hparameters
    '''

    (m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
    f, stride = hparameters['f'], hparameters['stride']

    n_H = int((n_H_prev - f) / stride + 1)
    n_W = int((n_W_prev - f) / stride + 1)
    n_C = n_C_prev

    A = np.zeros([m, n_H, n_W, n_C])

    for i in range(m):
        for h in range(n_H):
            vert_start = h * stride
            vert_end = vert_start + f
            for w in range(n_W):
                horiz_start = w * stride
                horiz_end = horiz_start + f
                for c in range(n_C):
                    a_slice_prev = A_prev[i, vert_start:vert_end, horiz_start:horiz_end, c]
                    
                    if mode == 'max':
                        A[i, h, w, c] = np.max(a_slice_prev)
                    elif mode == 'average':
                        A[i, h, w, c] = np.mean(a_slice_prev)

    cache = (A_prev, hparameters)
    assert(A.shape == (m, n_H, n_W, n_C))

    return A, cache

# test for pool forward
np.random.seed(1)
A_prev = np.random.randn(2,5,5,3)
hparameters = {'stride' : 1, 'f' : 3}

A, cache = pool_forward(A_prev, hparameters)
print("mode = max")
print("A.shape = " + str(A.shape))
print("A =\n", A)
print()
A, cache = pool_forward(A_prev, hparameters, mode = "average")
print("mode = average")
print("A.shape = " + str(A.shape))
print("A =\n", A)