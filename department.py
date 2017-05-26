# -*- coding: utf-8 -*-
import base64
def get_department(text):
	str=""
	for i in text :
		if "局" in i :
			k=i.find("局")
			return i[0:k]+"局"
			'''str="局"
			while k>=0 and k!=' ':
				str=str+i[k]
				k=k-1
			return str[::-1]'''
		elif "部" in i:
			k=i.find("部")
			return i[0:k]+"部"
			'''str="部"
			while k>=0 and k!=' ':
				str=str+i[k]
				k=k-1
			return str[::-1]'''
		elif "課" in i:
			k=i.find("課")
			return i[0:k]+"課"
			'''str="課"
			while k>=0 and k!=' ':
				str=str+i[k]
				k=k-1
			return str[::-1]'''
		elif "室" in i:
			k=i.find("室")
			return i[0:k]+"室"
			'''str="室"
			while k>=0 and k!=' ':
				str=str+i[k]
				k=k-1
			return str[::-1]'''
		elif "チーム" in i:
			k=i.find("チーム")
			return i[0:k]+"チーム"
			'''str="チーム"
			while k>=0 and k!=' ':
				str=str+i[k]
				k=k-1
			return str[::-1]'''
			