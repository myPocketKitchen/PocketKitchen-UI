import os
import sys
import logging

import numpy as np
import pandas as pd 

import gensim

# import config
from ingredient_parser import ingredient_parser

data = pd.read_csv('df_parsed.csv')
data['parsed_new'] = data.ingredients.apply(ingredient_parser)
data.head()

# get corpus with the documents sorted in alphabetical order
def get_and_sort_corpus(data):
    corpus_sorted = []
    for doc in data.parsed_new.values:
        doc.sort()
        corpus_sorted.append(doc)
    return corpus_sorted

corpus = get_and_sort_corpus(data)
print(f"Length of corpus: {len(corpus)}")
  
# calculate average length of each document 
lengths = [len(doc) for doc in corpus]
avg_len = float(sum(lengths)) / len(lengths)
avg_len

# train word2vec model 
sg = 0 # CBOW: build a language model that correctly predicts the center word given the context words in which the center word appears
workers = 4 # number of CPUs
window = 6 # window size: average length of each document 
min_count = 1 # unique ingredients are important to decide recipes 

model_cbow = gensim.models.Word2Vec(corpus, sg=sg, workers=workers, window=window, min_count=min_count, vector_size=100)

#Summarize the loaded model
print(model_cbow)

#Summarize vocabulary
words = list(model_cbow.wv.index_to_key)
words.sort()
# print(words)

#Acess vector for one word
#print(model_cbow.wv['egg'])

# most similar
# model_cbow.wv.most_similar(u'egg just larger than mushroom')
# model_cbow.wv.similarity('egg', 'egg just larger than mushroom')

model_cbow.save('model_cbow.bin')

loaded_model = gensim.models.Word2Vec.load('model_cbow.bin')
if loaded_model:
    print("Successfully loaded model")

class MeanEmbeddingVectorizer(object):

	def __init__(self, word_model):
		self.word_model = word_model
		self.vector_size = word_model.wv.vector_size

	def fit(self):  # comply with scikit-learn transformer requirement
		return self

	def transform(self, docs):  # comply with scikit-learn transformer requirement
		doc_word_vector = self.word_average_list(docs)
		return doc_word_vector

	def word_average(self, sent):
		"""
		Compute average word vector for a single doc/sentence.
		:param sent: list of sentence tokens
		:return:
			mean: float of averaging word vectors
		"""
		mean = []
		for word in sent:
			if word in self.word_model.wv.index_to_key:
				mean.append(self.word_model.wv.get_vector(word))

		if not mean:  # empty words
			# If a text is empty, return a vector of zeros.
			logging.warning("cannot compute average owing to no vector for {}".format(sent))
			return np.zeros(self.vector_size)
		else:
			mean = np.array(mean).mean(axis=0)
			return mean


	def word_average_list(self, docs):
		"""
		Compute average word vector for multiple docs, where docs had been tokenized.
		:param docs: list of sentence in list of separated tokens
		:return:
			array of average word vector in shape (len(docs),)
		"""
		return np.vstack([self.word_average(sent) for sent in docs])

mean_vec_tr = MeanEmbeddingVectorizer(loaded_model)
doc_vec = mean_vec_tr.transform(corpus)