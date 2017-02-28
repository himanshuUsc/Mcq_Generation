import re, math
from collections import Counter
import jellyfish as j 

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = u'I am happy.'
text2 = u'I am very happy.'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)
print"sentences are \n", text1,"\n",text2
print 'Cosine distance :', cosine







##########################################################
#--> JAro distance between sentences and other distance as well
lvd=j.damerau_levenshtein_distance((text1), (text2))
jd=j.jaro_winkler((text1), (text2))
print "levenshtein_distance :",lvd
print "Jaro distance :",jd 
