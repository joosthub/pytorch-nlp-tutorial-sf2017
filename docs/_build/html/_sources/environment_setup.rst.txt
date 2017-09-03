Environment Setup
=================

On this page, you will find not only the list of dependencies to install
for the tutorial, but a description of how to install them.

0. Get Anaconda
---------------

Anaconda is a Python (and R) distribution that aims to provide everything
needed for common scientific and machine learning situations out-of-the-box.

In practice, Anaconda can used to manage different environment and packages.
Our core instructions will assume that you have anaconda installed as your default
Python distribution.  When needed, we will include alternate instructions in case
you do not use Anaconda (though, you probably should).

You can download Anaconda here: https://www.continuum.io/downloads

After installing anaconda, you can access its command-line interface
with the :code:`conda` command.


1. Create a new environment
---------------------------

Environments are a tool for sanitary software development.  By this, we mean that
you can install specific versions of packages without worrying that it breaks
a dependency elsewhere.

Here is how you can create an environment with anaconda

.. code-block:: bash

   conda create -n dl4nlp python=3.6


2. Install Dependencies
-----------------------

After creating the environment, you need to **activate** the environment:

.. code-block:: bash

   source activate dl4nlp

After an environment is activated, it might prepend/append itself to your
console prompt to let you know it is active.

With the environment activated, any installation commands
(whether it is :code:`pip install X`, :code:`python setup.py install` or using
Anaconda's install command :code:`conda install X`) will only install inside
the environment.


There are some dependencies are not included in our :code:`requirements.txt`:

.. code-block:: bash

   conda install ipython
   conda install jupyter

   python -m ipykernel install --user --name dl4nlp


# install pytorch
# visit pytorch.org

# assume we are inside a folder dl4nlp
# note: that if you alternatively download the zip and unzip it to
#   a folder, it will be named something else
git clone https://github.com/joosthub/pytorch-nlp-tutorial.git
cd pytorch-nlp-tutorial

pip install -r requirements.txt

# going back to root folder
cd ..

# install torch text
git clone https://github.com/pytorch/text.git
cd text
python setup.py install
