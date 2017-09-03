Environment Setup
=================

On this page, you will find not only the list of dependencies to install
for the tutorial, but a description of how to install them. This tutorial assumes
you have a laptop with OSX or Linux. If you use Windows, you might have to install
a virtual machine to get a UNIX-like environment to continue with the rest of this
instruction. A lot of this instruction is more verbose than needed to accomodate 
participants of different skill levels.

0. Get Anaconda
---------------

Anaconda is a Python (and R) distribution that aims to provide everything
needed for common scientific and machine learning situations out-of-the-box. 
We chose Anaconda for this tutorial as it significantly simplifies Python 
dependency management. 

In practice, Anaconda can be used to manage different environment and packages.
This setup document will assume that you have anaconda installed as your default
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

2a. Activate the environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After creating the environment, you need to **activate** the environment:

.. code-block:: bash

   source activate dl4nlp

After an environment is activated, it might prepend/append itself to your
console prompt to let you know it is active.

With the environment activated, any installation commands
(whether it is :code:`pip install X`, :code:`python setup.py install` or using
Anaconda's install command :code:`conda install X`) will only install inside
the environment.

2b. Install IPython and Jupyter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We include a :code:`requirements.txt` for the core of the dependencies, but
there are some basic dependencies not included in it:

.. code-block:: bash

   conda install ipython
   conda install jupyter

To allow a jupyter notebooks to use this environment as their kernel, it
needs to be linked:

.. code-block:: bash

   python -m ipykernel install --user --name dl4nlp

2b1. Installing CUDA (for those with Nvidia GPU enabled laptops)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you have a CUDA compatible GPU, it is worthwhile to take advantage of it as 
it can significantly speedup training and make your PyTorch experimentation more
enjoyable.
1. Download CUDA appropriate to your OS/Arch from `here<https://developer.nvidia.com/cuda-downloads>`_.
2. Follow installation steps for your architecture/OS. For Ubuntu/x86_64, see `here<http://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#ubuntu-installation>`_
3. Download and install CUDNN from `here<https://developer.nvidia.com/cudnn>`_

Make sure you have the latest CUDA (8.0) and CUDNN (7.0).

2c. Install PyTorch
^^^^^^^^^^^^^^^^^^^

There are instructions on http://pytorch.org which detail how to install it.
If you have been following along so far and have anaconda installed with CUDA enabled, you can simply do:

.. code-block:: bash

   conda install pytorch torchvision cuda80 -c soumith

The widget on PyTorch.org will let you select the right commandline for your specific OS/Arch.
Make sure you have PyTorch 2.0 or higher.

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
