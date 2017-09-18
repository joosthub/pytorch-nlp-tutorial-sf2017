Exercise: Fast Lookups for Encoded Sequences
==========================================

Let's suppose that you want to embed or encode something that you want to look up at a later date.
For example, you could be embedded things that need to be identified (such as a song).  Or maybe you want to just find the neighbors of a new data point.

In any case, using the approximate nearest neighbors libraries are wonderful for this.
For this exercise, we will use Spotify's annoy library (we saw this on day 1, in the pretrained word vector notebook).  You should aim to complete the following steps:

1. Load the network from the Day 2, 01 notebook using the pre-trained weights.
    - You could use the 02 notebook, but we want to get a single vector per each sequence.
    - So, to use 02, you would need to port the :code:`column_gather` function.
    - One reason why you might be interested in doing this is because the 02 objective function learned a better final vector representation.
2. Given a loaded network with pre-trained weights, write a function which does nearly exactly what the forward function does, but doesn't apply the fully connected layer.
    - This is because we want the feature vector just before the fully connected.
    - it is common to assume that the penultimate layer has learned more generalizable features than the final layer (which is used in softmax computations and is this used to being normalize inducing a probability distribution).
    - The code for this shoud look something like:

.. code-block:: python

   def get_penultimate(net, x_in, x_lengths=None):
        x_in = net.emb(x_in)
        x_mid = net.conv(x_in.permute(0, 2, 1)).permute(0, 2, 1)
        y_out = net.rnn(x_in)

        if x_lengths is not None:
            y_out = column_gather(y_out, x_lengths)
        else:
            y_out = y_out[:, -1, :]

        return y_out

3. As you get penultimate vectors for each datapoint, store them in spotify's annoy. This requires specifying some label for the vector.  Using :code:`vectorizer.surname_vocab.lookup` is how you can retrieve the character for each index value in the network inputs.  There are some 'decode' functions in the day 2 02 and 03 notebooks.
4. Once everything is added to spotify's annoy, you can then look up any surname and find the set of nearest neighbors!  Kind of cool!  this is one way to do the `k nearest neighbor classification rule <https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm>`_.
