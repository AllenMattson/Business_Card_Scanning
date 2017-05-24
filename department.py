# -*- coding: utf-8 -*-
import base64
def get_department(text):
	for i in text :
		if "局" in i :
			k=i.find("局")
			return i[0:k]+"局"
		elif "部" in i:
			k=i.find("部")
			return i[0:k]+"部"
		elif "課" in i:
			k=i.find("課")
			return i[0:k]+"課"
		elif "室" in i:
			k=i.find("室")
			return i[0:k]+"室"
		elif "チーム" in i:
			k=i.find("チーム")
			return i[0:k]+"チーム"
			