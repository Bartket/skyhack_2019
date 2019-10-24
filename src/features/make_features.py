#%%
import pandas
from os import path
from importlib import reload
import shelve

from flair.data import Corpus
from flair.datasets import ClassificationCorpus
from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentRNNEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer

import src._utils as utils
utils = reload(utils)


#%%
data_folder = path.join('data', 'splitted_data')
train_data = utils.mgdb.read_mongo('raw_data_train')
train_data.to_csv(path.join(data_folder,'train.txt'),
                                               sep=' ',
                                               index=False,
                                               header=False,
                                               columns=['label', 'text'])

test_data = utils.mgdb.read_mongo('raw_data_test')
test_data.to_csv(path.join(data_folder, 'test.txt'),
                 sep=' ',
                 index=False,
                 header=False,
                 columns=['label', 'text'])

dev_data = utils.mgdb.read_mongo('raw_data_dev')
dev_data.to_csv(path.join(data_folder, 'dev.txt'),
                sep=' ',
                index=False,
                header=False,
                columns=['label', 'text'])

#%%
corpus: Corpus = ClassificationCorpus('data/splitted_data')
if len(corpus.train) ==0 or len(corpus.test) ==0:
    raise Exception('Creating corpus failed')


#%%
word_embeddings = [WordEmbeddings('glove')]

document_embeddings: DocumentRNNEmbeddings = DocumentRNNEmbeddings(
    word_embeddings,
    hidden_size=512,
    reproject_words=True,
    reproject_words_dimension=256,
)

label_dict = corpus.make_label_dictionary()

classifier = TextClassifier(document_embeddings, label_dictionary=label_dict)

#%%
with shelve.open(path.join('data', 'prepared_data', 'bbc')) as db:
    try:
        del db['classifier']
        del db['corpus']
    except:
        pass
    db['classifier'] = classifier
    db['corpus'] = corpus

#%%
