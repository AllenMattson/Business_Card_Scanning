# -*- coding: utf-8 -*-
import base64
def get_department(text):
	for i in text :
		if "局" in i :
			return i
		elif "部" in i:
			return i
		elif "課" in i:
			return i
		elif "室" in i:
			return i
		elif "チーム" in i:
			return i
			