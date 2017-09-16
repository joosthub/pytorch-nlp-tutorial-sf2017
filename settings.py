import os
from os.path import join


CUDA = bool(os.getenv('ENABLE_CUDA_DL4NLP', False))

ROOT_DIR = os.getenv('DL4NLPROOT', None)
if ROOT_DIR is None:
    ROOT_DIR = os.getenv('HOME', '.')
DATA_DIR = join(ROOT_DIR, 'data')
DAY1_DIR = join(ROOT_DIR, 'day1')
DAY2_DIR = join(ROOT_DIR, 'day2')
ZOO_DIR = join(ROOT_DIR, 'modelzoo')

GLOVE_FILENAME = join(DATA_DIR, 'glove.6B.100d.txt')

FIRSTNAMES_CSV = join(DATA_DIR, 'firstnames.csv')

SURNAMES_CSV = join(DATA_DIR, 'surnames.csv')

TRUMP_FILENAME = join(DATA_DIR, 'trump.csv')

AMAZON_FILENAME = join(DATA_DIR, 'amazon_train_small.csv')

SNLI_TRAIN_JSON = join(DATA_DIR, 'snli_1.0', 'snli_1.0_train.jsonl')
SNLI_DEV_JSON = join(DATA_DIR, 'snli_1.0', 'snli_1.0_dev.jsonl')
SNLI_TEST_JSON = join(DATA_DIR, 'snli_1.0', 'snli_1.0_test.jsonl')

ZHNEWS_CSV = join(DATA_DIR, 'zhnews.csv')

START_TOKEN = "^"
END_TOKEN= "_"

# used by pytorch backends to ignore non-classes in loss compuations
# best for sequences where not all things that go into the loss computation
# should be included in the loss
IGNORE_INDEX_VALUE = -1

class ZOO:
    charnn_surname_classifer = {
        'filename': join(ZOO_DIR,
                         'charnn_emb16_hid64_surnames_classify.state'),
        'vocab': join(ZOO_DIR, 'surnames_classify.vocab'),
        'comments': 'pre-trained surname classifier',
        'date': '09-14-2017',
        'parameters': {
            'embedding_size': 16,
            'hidden_size': 64
        }
    }
    charnn_surname_predicter = {
        'filename': join(ZOO_DIR,
                         'charnn_emb16_hid64_surnames_predict.state'),
        'vocab': join(ZOO_DIR, 'surnames_classify.vocab'),
        'comments': 'pre-trained surname sequence prediction (& generation model)',
        'date': '09-14-2017',
        'parameters': {
            'embedding_size': 16,
            'hidden_size': 64
        }
    }
    charnn_surname_conditioned_predicter = {
        'filename': join(ZOO_DIR,
                         'charnn_emb16_hid64_surnames_conditionally_predict.state'),
        'vocab': join(ZOO_DIR, 'surnames_classify.vocab'),
        'comments': 'pre-trained surname conditioned sequence prediction (& conditioned generation)',
        'date': '09-14-2017',
        'parameters': {
            'embedding_size': 16,
            'hidden_size': 64
        }
    }
    wordrnn_trump_tweet_predicter = {
        'filename': join(ZOO_DIR,
                         'wordrnn_emb100_hid64_trump_tweets_predict.state'),
        'vocab': join(ZOO_DIR, 'trump_twitter.vocab'),
        'comments': 'pre-trained trump sequence prediction (& generation)',
        'date': '09-14-2017',
        'parameters': {
            'embedding_size': 100,
            'hidden_size': 64
        }
    }
