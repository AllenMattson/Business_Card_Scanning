# -*- coding: utf-8 -*-
import base64
#!/usr/bin/python
import re


def check(text):
	line =text
	searchObj = re.search( r'[0-9]+-[0-9]+-[0-9]+', line, re.M|re.I)
	if searchObj != None and len(searchObj.group())<=8:
		return 1
	else :
		return 0

'''def floor_check(text):
	searchObj = re.search( r'[0-9]+F', line, re.M|re.I)
	if searchObj != None:
		return 1
	else :
		return 0'''
def check_postal_code(text):
	line =text
	searchObj = re.search( r'[0-9][0-9][0-9]-[0-9]{4} | [0-9]{7}', line, re.M|re.I)
	if searchObj != None and len(searchObj.group())<=8:
		return 1
	else :
		return 0



def get_address(text):
    str="〒"
    str1=""
    str2=""
    str3=""
    str4=""
    add=""
    for i in text:
        if str in i:
            str1=i
            add=add+i
        if "階" in i:
        	str2=i
        	if str2 not in add:
        		add=add+str2
        if check(i)==1:
        	str3=i
        	if str3 not in add:
        		add=add+str3
        if check_postal_code(i)==1:
        	str4=i
        	if str4 not in add:
        		add=add+str4


    


    return add


        

	