# Running this repository locally

During the training session, O'Reilly will be providing a JupyterHub for participants.
However, during that time and after the training ends, if you would like to run the contents of this repository, you can do so with the following steps:

1. Follow the instructions on [environment setup](http://dl4nlp.info/en/latest/environment_setup.html).
2. Download the files in the data/ and modelzoo/ folders.  The download link is in the `README.md` file in each respective folder.  The downloaded files will be zip files. They should be unzipped so that the files are inside these folders.
    - in other word, it should be `data/surnames.csv` etc.
    - Please make sure this is correct! It may unzip with an extra directory and be `data/data/surnames.csv` and this would be incorrect.
3. In a terminal with the `dl4nlp` (or equivalent) environment activated (see step 1 if you don't have this), navigate back to the top level (so you can see day_1, etc) and run the following command:

```bash
DL4NLPROOT=$(pwd) jupyter notebook --notebook-dir=$(pwd)
```

If you would like to run with CUDA enabled, please run:

```bash
ENABLE_CUDA_DL4NLP=1 DL4NLPROOT=$(pwd) jupyter notebook --notebook-dir=$(pwd)
```
