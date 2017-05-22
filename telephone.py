def count_number(text):
    count=0
    numb=""
    for i in range(0,len(text)):
        if text[i]>='0' and text[i]<='9':
            count=count+1
            numb=numb+text[i]
    return (count,numb)

def get_telephone_numb(text):
    #print "HT"
    #print "Himasnhu",count_number("9646456964")
    str=""
    
    '''for i in text:
        #print i
        if "TEL:" in i:

            k=i.find("FAX:")
            #print "Himanshu"
            #print k
            if i[4]==' ':
                #print i[5:k]
                #print"YES"
                if k!=-1:
                    return i[5:k]
            else :
                if k!=-1:
                    return i[4:k]

        elif "Tel:" in i:
            #return i
            k=i.find("Fax:")
            #print k
            if i[4]==' ':
                #print i[5:k]
                if k!=-1:
                    return i[5:k]
            else :
                if k!=-1:
                    return i[4:k]

        elif "T." in i:
            #return i
            k=i.find("F.")
            #print k
            if i[4]==' ':
                if k!=-1:
                #print i[5:k]
                    return i[3:k]
            else :
                if k!=-1:
                    return i[2:k]


        elif "Tel." in i:
            #return i
            k=i.find("Fax.")
            #print k
            if i[4]==' ':
                #print i[5:k]
                return i[5:k]
            else :
                return i[4:k]

        if "TEL:" in i and "FAX" not in i:
            if i[4]==' ':
                return i[5:]
            else:
                return i[4:]


        elif "Tel:" in i and "Fax" not in i:
            #print "HT"
            if i[4]==' ':
                #print "Himanshu",i[5:]
                return i[5:]
            else:
                return i[4:]

        elif "T." in i and "F" not in i:
            if i[4]==' ':
                return i[5:]
            else:
                return i[4:]

        if "Tel" in i:
            k=i.find("Tel")
            j=k+3
            #print ord('A')
            while  j<len(i) and (ord(i[j])<48 or ord(i[j])>57 ):
                j=j+1;

            if j<len(i):
                l=j
                str=""
                while( l<len(i) and (i[l]>='0' and i[l]<='9') or i[l]=='-'):
                    str=str+i[l]
                    l=l+1
            #print str
                if len(str)==12:
                    return str

        elif "TEL" in i:
            k=i.find("TEL")
            j=k+3
            #print ord('A')
            while  j<len(i) and (ord(i[j])<48 or ord(i[j])>57 ):
                j=j+1;

            if j<len(i):
                l=j
                str=""
                while( l<len(i) and (i[l]>='0' and i[l]<='9') or i[l]=='-'):
                    str=str+i[l]
                    l=l+1
            #print str
                if len(str)==12:
                    return str

        elif "T" in i:
            k=i.find("T")
            j=k+1
            #print ord('A')

            while  j<len(i) and (ord(i[j])<48 or ord(i[j])>57 ):
                j=j+1;

            if j<len(i):
                l=j
                str=""
                while( l<len(i) and (i[l]>='0' and i[l]<='9') or i[l]=='-'):
                    str=str+i[l]
                    l=l+1
            #print str
                if len(str)==12:
                    return str'''

    for i in text:
        if "TEL" in i:
            k=i.find("TEL")
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
           

        elif "Tel" in i:
            k=i.find("Tel")
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
           

        elif "T" in i:
            k=i.find("T")
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

           


        elif "P" in i:
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
        if counter ==10:
            return (str)
        elif counter == 11:
            return str
        elif counter==12:
            return str





            

