Compute Convolution Sizes
=========================


.. code-block:: python

   import math

   def conv_shape_helper_1d(input_seq_len, kernel_size, stride=1, padding=0, dilation=1):
       kernel_width = dilation * (kernel_size - 1) + 1
       tensor_size = input_seq_len + 2 * padding
       return math.floor((tensor_size - kernel_width) / stride + 1)
