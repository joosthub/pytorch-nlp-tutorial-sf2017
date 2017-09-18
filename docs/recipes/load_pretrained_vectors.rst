Loading Pretrained Vectors
==========================

It can be extremely useful to make a model which had as advantageous starting point.

To do this, we can set the values of the embedding matrix.


.. code-block:: python

   # we give an example of this function in the day 1, word vector notebook
   word_to_index, word_vectors, word_vector_size = load_word_vectors()


   # now, we want to iterate over our vocabulary items
   for word, emb_index in vectorizer.word_vocab.items():
       # if the word is in the loaded glove vectors
       if word.lower() in word_to_index:
            # get the index into the glove vectors
            glove_index = word_to_index[word.lower()]
            # get the glove vector itself and convert to pytorch structure
            glove_vec = torch.FloatTensor(word_vectors[glove_index])

            # this only matters if using cuda :)
            if settings.CUDA:
                glove_vec = glove_vec.cuda()

            # finally, if net is our network, and emb is the embedding layer:
            net.emb.weight.data[emb_index, :].set_(glove_vec)
