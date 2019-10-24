#%%
from flair.data import Corpus
from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentRNNEmbeddings
from flair.models import TextClassifier
from flair.trainers import ModelTrainer

import shelve
from os import path

#%% Loading classifier
with shelve.open(path.join('data', 'prepared_data', 'bbc')) as db:
    classifier = db['classifier']
    corpus=db['corpus']

#%% Model trainer definition
trainer = ModelTrainer(classifier, corpus)
model_path = path.join('models', 'bbc')

# 7. start the training
trainer.train(model_path,
              learning_rate=0.1,
              mini_batch_size=32,
              anneal_factor=0.5,
              patience=5,
              max_epochs=150)

# 8. plot weight traces (optional)
from flair.visual.training_curves import Plotter
plotter = Plotter()
plotter.plot_training_curves(path.join(model_path, 'loss.tsv'))
plotter.plot_weights(path.join(model_path, 'weights.txt'))
#%%
