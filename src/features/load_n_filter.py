#%%
import pandas as pd
from sklearn import model_selection

import src._utils as uts


#%% Load
data = uts.mgdb.read_mongo('raw_data')


#%% Filter tha data
# PASS

data.loc[:, 'label'] = '__label__' + data.loc[:, 'label'].astype(str)

#%% Split dataset to train and test
mask = model_selection.train_test_split(data, test_size=0.25)

train_data = mask[0]
test_data = mask[1]

# Split test set into dev(10%) and test(15%)
mask = model_selection.train_test_split(test_data, test_size=0.4)
test_data = mask[0]
dev_data = mask[1]

del mask

#%% Save split into mongo
uts.mgdb.write_mongo(test_data, 'raw_data_test')
uts.mgdb.write_mongo(train_data, 'raw_data_train')
uts.mgdb.write_mongo(dev_data, 'raw_data_dev')


#%%
