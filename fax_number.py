def count_number(text):
    count=0
    numb=""
    for i in range(0,len(text)):
        if text[i]>='0' and text[i]<='9':
            count=count+1
            numb=numb+text[i]
    return (count,numb)

def get_fax_numb(text):
    '''print len("Himanshu")
    for i in text:
        if "FAX:" in i:
            k=i.find("FAX:")
            #print k
            if k+4==' ':
                return i[k+5:]
            else:
                return i[k+4:]

        if "Fax:" in i:
            k=i.find("Fax:")
            #print k
            if k+4==' ':
                return i[k+5:]
            else:
                return i[k+4:]

        if "F." in i:
            k=i.find("F.")
            #print k
            if k+2==' ':
                return i[k+3:]
            else:
                return i[k+2:]



        if "FAX." in i:
            k=i.find("FAX.")
            #print k
            if k+4==' ':
                return i[k+5:]
            else:
                return i[k+4:]

        if "Fax." in i:
            k=i.find("Fax.")
            #print k
            if k+4==' ':
                return i[k+5:]
            else:
                return i[k+4:]

        if "Fax" in i:
            k=i.find("Fax")
            #print i
            #print len(i)
            j=k+3
            #print ord('A')
            while  j<len(i) and (ord(i[j])<48 or ord(i[j])>57 ):
                j=j+1;
            #print j
            if j<len(i):
                l=j
                str=""
                while( l<len(i) and (i[l]>='0' and i[l]<='9') or i[l]=='-'):
                    str=str+i[l]
                    #print i[l]
                    l=l+1
                    if l>=len(i):
                        break
            #print str
                if len(str)==12:
                    return str

        if "FAX" in i:
            k=i.find("FAX")
            #print i
            #print len(i)
            j=k+3
            #print ord('A')
            while  j<len(i) and (ord(i[j])<48 or ord(i[j])>57 ):
                j=j+1;
            #print j
            if j<len(i):
                l=j
                str=""
                while( l<len(i) and (i[l]>='0' and i[l]<='9') or i[l]=='-'):
                    str=str+i[l]
                    #print i[l]
                    l=l+1
                    if l>=len(i):
                        break
            #print str
                if len(str)==12:
                    return str


        if "F" in i:
            k=i.find("F")
            #print i
            #print len(i)
            j=k+3
            #print ord('A')
            while  j<len(i) and (ord(i[j])<48 or ord(i[j])>57 ):
                j=j+1;
            #print j
            if j<len(i):
                l=j
                str=""
                while( l<len(i) and (i[l]>='0' and i[l]<='9') or i[l]=='-'):
                    str=str+i[l]
                    #print i[l]
                    l=l+1
                    if l>=len(i):
                        break
            #print str
                if len(str)==12:
                    return str'''
    str=""

    for i in text:
        if "FAX" in i:
            k=i.find("FAX")
            #print "Himanshu"
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
           

        elif "Fax" in i:
            k=i.find("Fax")
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
           

        elif "F" in i:
            k=i.find("F")
            j=k+1
            while (j<len(i) and ((ord(i[j])<48) or (ord(i[j])>57)) and i[j]!="+"):
                j=j+1

            if j<len(i):
                l=j
                
                while(l<len(i) and ((i[l]>='0' and i[l]<='9') or i[l]=="(" or i[l]==")" or i[l]=="-" or i[l]=="+") or i[l]==" "):
                    if i[l]=="(" or i[l]==" " or i[l]==")":
                        l=l+1
                        continue
                    else :
                        str=str+i[l]
                        l=l+1

           


        elif "f" in i:
            k=i.find("f")
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

        
        #print str
        counter,number=count_number(str)
        if counter ==10:
            return (str)
        elif counter == 11:
            return str
        elif counter==12:
            return str