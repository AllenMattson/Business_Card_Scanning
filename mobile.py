# -*- coding: utf-8 -*-
import base64
def count_number(text):
    count=0
    numb=""
    for i in range(0,len(text)):
        if text[i]>='0' and text[i]<='9':
            count=count+1
            numb=numb+text[i]
    return (count,numb)

def get_mobile_numb(text):
    #print "HT"
    #print "Himasnhu",count_number("9646456964")
    str=""
    
   
    for i in text:
        if "MOB" in i:
            k=i.find("MOB")
            j=k+1
            while (j<len(i) and ((ord(i[j])<48) or (ord(i[j])>57)) and i[j]!="+"):
                j=j+1
            #print "Himanshu"
            if j<len(i):
                l=j
                
                while(l<len(i) and ((i[l]>='0' and i[l]<='9') or i[l]=="(" or i[l]==")" or i[l]=="-" or i[l]=="+" or i[l]==" ")):
                    #print i[l]
                    if i[l]=="(" or i[l]==" " or i[l]==")":
                        l=l+1
                        continue
                    else :
                        str=str+i[l]
                        l=l+1
           

        elif "Mob" in i:
            k=i.find("Mob")
            j=k+1
            while (j<len(i) and ((ord(i[j])<48) or (ord(i[j])>57)) and i[j]!="+"):
                j=j+1

            if j<len(i):
                l=j
                
                while(l<len(i) and ((i[l]>='0' and i[l]<='9') or i[l]=="(" or i[l]==")" or i[l]=="-" or i[l]=="+" or i[l]==" ")):
                    if i[l]=="(" or i[l]==" " or i[l]==")":
                        l=l+1
                        continue
                    else :
                        str=str+i[l]
                        l=l+1
           

        elif "M" in i:
            k=i.find("M")
            j=k+1
            while (j<len(i) and ((ord(i[j])<48) or (ord(i[j])>57)) and i[j]!="+"):
                j=j+1

            if j<len(i):
                l=j
                
                while((l<len(i) and ((i[l]>='0' and i[l]<='9') or i[l]=="(" or i[l]==")" or i[l]=="-" or i[l]=="+") or i[l]==" ")):
                    #print l,len(i),i
                    if i[l]=="(" or i[l]==" " or i[l]==")":
                        l=l+1
                    elif i[l]=='\n':
                        break
                    else :
                        str=str+i[l]
                        l=l+1

                    if l==len(i):
                        break


        elif "m" in i:
            k=i.find("m")
            j=k+1
            while (j<len(i) and ((ord(i[j])<48) or (ord(i[j])>57)) and i[j]!="+"):
                j=j+1

            if j<len(i):
                l=j
                
                while((l<len(i) and ((i[l]>='0' and i[l]<='9') or i[l]=="(" or i[l]==")" or i[l]=="-" or i[l]=="+") or i[l]==" ")):
                    #print l,len(i),i
                    if i[l]=="(" or i[l]==" " or i[l]==")":
                        l=l+1
                    elif i[l]=='\n':
                        break
                    else :
                        str=str+i[l]
                        l=l+1

                    if l==len(i):
                        break

           


        elif "携帯" in i:
            k=i.find("P")
            j=k+1
            while (j<len(i) and ((ord(i[j])<48) or (ord(i[j])>57)) and i[j]!="+"):
                j=j+1

            if j<len(i):
                l=j
                
                while(l<len(i) and ((i[l]>='0' and i[l]<='9') or i[l]=="(" or i[l]==")" or i[l]=="-" or i[l]=="+" or i[l]==" ")):
                    if i[l]=="(" or i[l]==" " or i[l]==")":
                        l=l+1
                        continue
                    else :
                        str=str+i[l]
                        l=l+1

        

        counter,number=count_number(str)
        #print counter,str,i
        if counter ==10:
            return (str)
        elif counter == 11:
            return str
        elif counter==12:
            return str
        else :
            str=""
            continue





            

