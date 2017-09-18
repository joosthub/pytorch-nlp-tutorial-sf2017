A New Load-Vectorize-Generate
=============================

In this exercise, you should look into the two datasets that are not included in the exercises.  There are two datasets to work with.  The first is the Amazon Review dataset.

.. code-block:: python

   from local_settings import settings
   import pandas as pd

   data = pd.read_csv(settings.AMAZON_FILENAME, names=['rating', 'title', 'review'])
   print(data.head())

The Amazon Reviews Dataset does not come with a precompute train-test split. One thing that would be important is to select a subset to do that.

The other is the first names dataset.  You can load with:

.. code-block:: python

   from local_settings import settings
   import pandas as pd

   data = pd.read_csv(settings.FIRSTNAMES_CSV)
   print(data.head())


For these two datasets, you should write a Raw dataset which loads the data. Then, you should write a Vectorizer which creates the relevant vocabularies from the 'fit' method and transforms a raw dataset into a vectorized dataset using the 'transform' method.  Finally, you should write a Vectorized datset which implements the required :code:`__len__` and :code:`__getitem__` methods.

The make_generator can be reused.
