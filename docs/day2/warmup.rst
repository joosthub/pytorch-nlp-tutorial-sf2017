Warm Up Exercise
================

To get you back into the PyTorch groove, let's do some easy exercises. You will have 10 minutes.  See how far you can get.

1. Use :code:`torch.randn` to create two tensors of size (29, 30, 32) and and (32, 100).
2. Use :code:`torch.matmul` to matrix multiply the two tensors.
3. Use :code:`torch.sum` on the resulting tensor, passing the optional argument of :code:`dim=1` to sum across the 1st dimension.  Before you run this, can you predict the size?
4. Create a new long tensor of size (3, 10) from the :code:`np.random.randint` method.
5. Use this new long tensor to index into the tensor from step 3.
6. Use :code:`torch.mean` to average across the last dimension in the tensor from step 5.
