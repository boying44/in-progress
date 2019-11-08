from sklearn.datasets import fetch_20newsgroups
train = fetch_20newsgroups(subset='train', shuffle = True)
test = fetch_20newsgroups(subset='test', shuffle = True)

print(list(train.target_names))

import * from gensim
print(genism.utils.simple_preprocess(train))