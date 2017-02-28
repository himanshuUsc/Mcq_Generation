import pickle
from practnlptools.tools import Annotator
import random
import Levenshtein as d
import gensim
import numpy as np
import scipy as sp
from scipy import spatial


def avg_feature_vector(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        index2word_set=[]
        nwords = 0

        #list containing names of words in the vocabulary
        #index2word_set = set(model.index2word) this is moved as input param for performance reasons
        # index2word_set = set(model.index2word)
        for word in words:
            if word in index2word_set:
                nwords = nwords+1
                featureVec = np.add(featureVec, model[word])

        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec

annotator=Annotator()
documents=pickle.load(open("questions_list.pkl","rb"))

a=pickle.load(open("keyword_list.pkl","rb"))
#dictionary contains the keywords:question list from the database
d=pickle.load(open("keyword_ques_dict.pkl","rb"))
length_key=len(d)
stoplist = set('for a of the and to in'.split())
word2vec_model = gensim.models.Word2Vec(documents, size=100)
word2vec_model.train(documents)
# print(dir(word2vec_model))
# o=set(word2vec_model)
# print(word2vec_model.similarity('krugman', 'obama'))
# index2word_set = set(word2vec_model.index2word)
sentence_1 = "this is sentence number one"
index_list=documents
sentence_1_avg_vector = avg_feature_vector(sentence_1.split(), model=word2vec_model, num_features=300)

#get average vector for sentence 2
sentence_2 = "this is sentence number two"
sentence_2_avg_vector = avg_feature_vector(sentence_2.split(), model=word2vec_model, num_features=300)
print(sentence_2_avg_vector)

sen1_sen2_similarity =  1 - spatial.distance.cosine(sentence_1_avg_vector,sentence_2_avg_vector)

print("similarity is, ",sen1_sen2_similarity)