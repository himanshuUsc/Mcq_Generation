import xml.etree.ElementTree as ET
import re
import pickle
tree = ET.parse('data.xml')
root = tree.getroot()

# print(root.tag)
# print(root.attrib)
keyword_list=[]

id_list=[]
final_dict={}
a=root.getchildren
for child in root:
	# print(type(child.attrib))
	keyword_list.append(child.attrib['text'])
	question_list=[]
	for subchild in child:
		
		x=subchild.tag
		y=subchild.attrib
		# print(subchild.tag,y)
		c=child.getchildren()
		# print(c.text)
		
		for i in c:
			# print("i ka tag is ",i.tag)
			x=i.getchildren()
			for k in x:
				# print("tag is ", (k.attrib))
				# print("text is ", type(k.text))
				s=k.text
				question=s.split("\n\t")
				# print(k)
				# h=s.split("\t")
				# print(h[1])
				# s2=' '.join(s.split('\n \t'))
				# # print(type(s))
				# print(s)
				question_list.append(question[1].strip())
				final_dict[child.attrib['text']]=question_list
		# for i in c:
		# 	print(c)
		# 	print((i.getchildren()[0].text))
# print(final_dict['Jon Bon Jovi'])
# t=[]
# t = map(lambda question_list: question_list.strip(), t)
# print(t)
# print(len(question_list))	
# print(len(attribute_list)	)
# f=open("questions_list.pkl","wb")
# pickle.dump(question_list,f)
f2=open("keyword_ques_dict.pkl","wb")
pickle.dump(final_dict,f2)
# print(len(keyword_list))