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
import codecs
import random
import pickle
# f = codecs.open('unicode.rst', encoding='utf-8')


annotator=Annotator()
# docs=pickle.load(open('questions_list.pkl','rb'))
# print len(docs)

with codecs.open('2.txt',encoding='utf-8',mode='r') as f :
	lines = f.readlines()
	
	# print lines.split("\t")
	# print lines
lines=[x.strip() for x in lines]
# print lines
docs=[]
for line in lines:
	x=line.split("\t")
	# print x[3]
	docs.append(x[3])
# print len(docs)


class LabeledLineSentence(object):
    def __init__(self, sources):
        self.sources = sources
        # print("iniint se ",sources[0])
        
        
    def __iter__(self):
    	# print(self.sourcegensim.s)
    	prefix="SENT_"
        for i in range(len(self.sources)):
            yield gensim.models.doc2vec.LabeledSentence(gensim.utils.to_unicode(self.sources[i]).split(), [prefix + '_%s' % i])
    
    def to_array(self):
        self.sentences = []
        prefix="SENT_"
        for i in range(len(self.sources)):
                    self.sentences.append(gensim.models.doc2vec.LabeledSentence(gensim.utils.to_unicode(self.sources[i]).split(), [prefix + '_%s' % i]))
        # print(self.sentences)
        return self.sentences
    
    def sentences_perm(self):
        shuffle(self.sentences)
        return self.sentences
def get_key(sentence):

	ques=sentence
	x= annotator.getAnnotations(ques.encode('utf-8'))['srl']
	y= annotator.getAnnotations(ques.encode('utf-8'))['ner']
	c=1
	new=''
	loc1=''
	# print "question is \n\n ",ques
	# print x
	# print y
	for j in range(len(y)):
		temp = y[j]
		# print temp[1]
		if  ((temp[1]=='S-PER' or temp=='E-PER' or temp=='B-PER' or temp=='E-ORG' or temp[1]=='S-MISC' or temp=='S-ORG' or temp=='B-MISC' or temp=='E-MISC' or temp=='B-ORG' ) and c==1):
			loc1=str(temp[0])
			# print j," answer is ",loc1
			
			# new= ques.replace(loc1,"_______",1)
			# print ques
			c=c+1
	

		elif ((temp[1]=='S-LOC' or temp[1]=='E-LOC' or temp[1]=='S-MISC' or temp=='B-MISC') and c==1):
			loc1=str(temp[0])
			# print j,"answer is ",loc1
			
			# new= ques.replace(str(loc1),"_______",1)
			# print ques
			c=c+1
	

	# print "old ques is ", ques
	# print "question is \n",new,'\n'
	return loc1
	# print "candidate answers are \n"

def print_question(ques,answer,dist):
	question=ques.replace(answer,"_________",1)
	print "Question is \n\n",question
	try:
		if answer != '':
			print str(1)+' ) ',answer
	except:
		print str(1)+' ) ','nota'
	dist=list(set(dist))
	final=[]
	final.append(answer)
	while '' in dist:
		dist.remove('')
	# print "distractors are ", dist
	try:
		if len(dist)<4:
			# print ("len of options is not huge")
			for i in range(5):
				dist.append("none of the above")
			# print "len of distractors became", len(dist)
	except:
		print "questions is not informative"
	c=1
	for j in range(len(dist)):
		if (answer == dist[j]) or ( answer==''):
			# print "in blansk"
			# print "dist is ", dist[j]
			continue
		else:
			# print "in correct "
			c=c+1
			if c<5:
				print c,") ", dist[j] 
				final.append(dist[j])
	# print dist

	
	


def get_questions(model,sentence):
	ques=sentence[0]
	cques=sentence[1:]
	answer=get_key(ques)
	# print answer 
	distractors=[]
	for j in range(len(cques)):
		distractors.append(get_key(cques[j]))
	
	print_question(ques,answer,distractors)


	

	# candidate=sentence[1:]
	# for i in range(len(candidate)):
	# 	can_ques=candidate[i]
	# 	x= annotator.getAnnotations(can_ques.encode('utf-8'))['srl']
	# 	y= annotator.getAnnotations(can_ques.encode('utf-8'))['ner']
	# 	loc2=''

	# 	for j in range(len(y)):
	# 		# print "inside candidate"
	# 		temp = y[j]
	# 		# print temp

	# 		if temp[1]=='S-LOC' or temp[1]=='E-LOC':
	# 			# print "hi hi i"
	# 			loc2=str(temp[0])
	# 			print loc2

	# 	print i+1,") ",loc2
				
				

	# 	for a in range(len(temp)):
	# 		print temp

if __name__ == '__main__':
	A=LabeledLineSentence(docs)

	# print(dir(A))
	# print(A.documents)

	# print("inside train")
	model = gensim.models.Doc2Vec(alpha=0.025, min_alpha=0.025)  # use fixed learning rate
	# print(model)
  	# s=A.to_array()
  	# print(s)
	 
	# model.build_vocab(s)
	# for epoch in range(50):
	# 	print(epoch)
	# 	model.train(A.sentences_perm())
	# 	model.alpha -= 0.002
	# 	model.min_alpha = model.alpha
	# model.save('train3.doc2vec')
	model=gensim.models.Doc2Vec.load('train3.doc2vec')
	# # print(model)
	# # x=9
	# # print(words[x])
	# # print(repr(model))
	# # print "hi"
	print 
	x= random.randint(0,len(docs))
	q='SENT__'+str(x)
	print "qno is ",q
	# print docs[x]
	
	final=[]
	# try:
	ans=model.docvecs.most_similar(q)
	# print "\n\n\n result is ",ans,"\n"
	# print "Question to be generated is \n"
	# print '\n',docs[x]
	final.append(docs[x])
	# print "srl and ner is  ", get_key(docs[x])
	# print "\ncandidate sentences are \n"
	for i in range(len(ans)):
		temp=ans[i][0]
		# print(temp)
		new=''
		z=int(temp.replace('SENT__',''))
		# print(z)
		# print "%s"%i,')'+docs[z]
		try:
			final.append(docs[z])
		except:
			pass
		# print "srl and ner is  ", get_key(docs[z])
	print "\n\n"
	# print final
	get_questions(model,final)
# except:
	# print "questions not in the training data "



