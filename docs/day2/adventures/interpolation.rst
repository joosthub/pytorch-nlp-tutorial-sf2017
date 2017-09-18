Exercise: Interpolating Between Vectors
=======================================

One fun option for the conditional generation code is to interpolate
between the learned hidden vectors.

To do this, first look at the code for sampling given a specific nationality:

.. code-block:: python
   :linenos:

   def sample_n_for_nationality(nationality, n=10, temp=0.8):
        assert nationality in vectorizer.nationality_vocab.keys(), 'not a nationality we trained on'
        keys = [nationality] * n
        init_vector = long_variable([vectorizer.nationality_vocab[key] for key in keys])
        init_vector = net.conditional_emb(init_vector)
        samples = decode_matrix(vectorizer,
                            sample(net.emb, net.rnn, net.fc,
                                   init_vector,
                                   make_initial_x(n, vectorizer),
                                   temp=temp))
        return list(zip(keys, samples))

As you can see, we create a list of keys that is the length of the number of samples we want (n).
And we use that list to retrieve the correct index from the vocabulary.
Finally, we use that index in the conditional embedding inside the network to get the
initial hidden state for the sampler.

To do this exercise, write a function that has the following signature:

.. code-block:: python

   def interpolate_n_samples_from_two_nationalities(nationality1, nationality2, weight, n=10, temp=0.8):
       print('awesome stuff here')


This should retrieve the :code:`init_vectors` for two different nationalities. Then, using the weight, combine the init vectors as :code:`weight * init_vector1 + (1 - weight) * init_vector2`.

For fun, after you finish this function, write a for loop which loops over the weight from 0.1 to 0.9 to see how it affects the generation.
