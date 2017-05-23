# -*- coding: utf-8 -*-
import base64
def get_company_name(text):
	for i in text:
		if "株式会社" in i:
			return i
		elif "協会" in i :
			return i
		elif "Co. Ltd" in i:
			return i
		elif "Assocciation" in i:
			return i
		elif "大使館"in i:
			return i
		elif "リミテッド" in i:
			return i
		elif "有限会社" in i:
			return i
		elif "大學" in i:
			return i
