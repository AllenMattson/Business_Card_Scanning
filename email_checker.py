# -*- coding: utf-8 -*-
import base64
#!/usr/bin/python
import re

def edit_email (text):
	text1 = re.sub(r' ', "", text)
	text2 = re.sub(r'Email:',"",text1)
	text3 = re.sub(r'email:',"",text2)
	text4 = re.sub(r'email',"",text3)
	text5 = re.sub(r'Email',"",text4)
	text6 = re.sub(r'。',"",text5)
	text7 = re.sub(r',',".",text6)
	text8 = re.sub(r'E-mail',"",text7)
	text9 = re.sub(r':',"",text8)
	return text9
	