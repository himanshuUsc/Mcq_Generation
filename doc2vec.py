import pickle
from practnlptools.tools import Annotator
import random
import Levenshtein as d
import gensim
import numpy as np
import scipy as sp
from scipy import spatial
from nltk.corpus import stopwords
import random
from random import shuffle


from practnlptools.tools import Annotator


documents=pickle.load(open("questions_list.pkl","rb"))
# print(documents)
annotator=Annotator()

a=pickle.load(open("keyword_list.pkl","rb"))
#dictionary contains the keywords:question list from the database
d=pickle.load(open("keyword_ques_dict.pkl","rb"))

# print(documents)
words=[]
for i in range(len(documents)):
	x=(documents[i].split())
	for j in range(len(x)):
		words.append(x[j])
# print(len(words))
x=[]
stop=set(stopwords.words('english'))
# print(stop)
for j in range(len(words)):
	# print(words[j])
	if words[j]  not in stop:
		x.append(words[j])
# print(len(words))
# print(x)

# print a
# print d
def get_key(sentence):
	srl=annotator.getAnnotations(sentence.encode('utf-8'))['srl']
	ner=annotator.getAnnotations(sentence.encode('utf-8'))['ner']
	try :
		print sentence
		print srl
		# if 


	except:
		print "no keywords found in this sentence"

for j in documents:
	get_key(j)
# class LabeledLineSentence(object):
#     def __init__(self, documents):
#         self.documents = documents
#         # print(documents)
#     def __iter__(self):
#     	# print(documents)
#         for i in range(len(documents)):
# 			# print(i)
# 			yield gensim.models.doc2vec.LabeledSentence(words=documents[i].split(), tags=['SENT_%s' % i])
# 			print(LabeledSentence)
# class LabeledLineSentence(object):
#     def __init__(self, sources):
#         self.sources = sources
#         # print("iniint se ",sources[0])
        
        
#     def __iter__(self):
#     	# print(self.sourcegensim.s)
#     	prefix="SENT_"
#         for i in range(len(self.sources)):
#             yield gensim.models.doc2vec.LabeledSentence(gensim.utils.to_unicode(self.sources[i]).split(), [prefix + '_%s' % i])
    
#     def to_array(self):
#         self.sentences = []
#         prefix="SENT_"
#         for i in range(len(self.sources)):
#                     self.sentences.append(gensim.models.doc2vec.LabeledSentence(gensim.utils.to_unicode(self.sources[i]).split(), [prefix + '_%s' % i]))
#         # print(self.sentences)
#         return self.sentences
    
#     def sentences_perm(self):
#         shuffle(self.sentences)
#         return self.sentences
	

# if __name__ == '__main__':
# 	A=LabeledLineSentence(documents)

# 	# print(dir(A))
# 	# print(A.documents)

# 	# print("inside train")
# 	model = gensim.models.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
# 	# print(model)
#  #  	s=A.to_array()
#  #  	print(s)
	 
# 	# model.build_vocab(s)
# 	# for epoch in range(50):
# 	# 	print(epoch)
# 	# 	model.train(A.sentences_perm())
# 	# 	model.alpha -= 0.002
# 	# 	model.min_alpha = model.alpha
# 	# model.save('train1.doc2vec')
# 	model=gensim.models.Doc2Vec.load('train1.doc2vec')
# 	# print(model)
# 	# x=9
# 	# print(words[x])
# 	# print(repr(model))
# 	print "hi"
# 	x=222
# 	q='SENT__'+str(x)
	

# 	ans=model.docvecs.most_similar(q)
# 	print "\n\n\n result is ",ans,"\n"
# 	print "Question to be generated is \n"
# 	print '\n',documents[x]
# 	print "\ncandidate sentences are \n"
# 	for i in range(len(ans)):
# 		temp=ans[i][0]
# 		# print(temp)
# 		new=''
# 		z=int(temp.replace('SENT__',''))
# 		# print(z)
# 		print "%s"%i,')'+documents[z]
# 	print "\n\n"