# -*- coding: utf-8 -*-
import base64

def get_position(text):
	'''for i in text :
		if "大使" in i :
			k=i.find("大使")
			return i[0:k]+"大使"
		elif "委員" in i:
			k=i.find("委員")
			return i[0:k]+"委員"
		elif "係長" in i:
			k=i.find("係長")
			return i[0:k]+"係長"
		elif "主任" in i:
			k=i.find("主任")
			return i[0:k]+"室"
		elif "副主任" in i:
			k=i.find("副主任")
			return i[0:k]+"副主任"
		elif "課長" in i:
			k=i.find("課長")
			return i[0:k]+"課長"
		elif "副課長" in i:
			k=i.find("副課長")
			return i[0:k]+"副課長"
		elif "主査" in i:
			k=i.find("主査")
			return i[0:k]+"主査"
		elif "副主査" in i:
			k=i.find("副主査")
			return i[0:k]+"副主査"
		elif "センター長" in i:
			k=i.find("センター長")
			return i[0:k]+"センター長"
		elif "社長" in i:
			k=i.find("社長")
			return i[0:k]+"社長"
		elif "部長" in i:
			k=i.find("部長")
			return i[0:k]+"部長"
		elif "支店長" in i:
			k=i.find("支店長")
			return i[0:k]+"支店長"
		elif "監査役" in i:
			return i'''

	with open('position.txt') as f:
    		content= f.readlines()
    		content = [x.strip() for x in content] 



    	for j in text:
    		for i in content :
    			#print i
    			if i in j:
    				#print i
    				#print "HT ",j
    				return j

