# -*- coding: utf-8 -*-
import base64
import requests
import nltk
from telephone import get_telephone_numb
from fax_number import get_fax_numb
from company_name import get_company_name


def detect_text(image_file):

    with open(image_file, 'rb') as image:
        base64_image = base64.b64encode(image.read()).decode()

    #print "Himanshu"
    url = 'https://vision.googleapis.com/v1/images:annotate?key=API KEY HERE'
    header = {'Content-Type': 'application/json'}
    body = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                'type': 'TEXT_DETECTION',
                'maxResults': 1,
            }]

        }]
    }
    response = requests.post(url, headers=header, json=body).json()
    #print "Response"
    #print response

    text = response['responses'][0]['textAnnotations'][0]['description'] if len(response['responses'][0]) > 0 else ''
    print text.encode('utf_8')
    return text.encode('utf_8')



def get_web_address(text):
    for i in text:
        if "www" in i:
            k=i.find("www")
            str=""
            j=k
            while(j<len(i)):
                str=str+i[j]
                j=j+1
            return str
        if "WWW" in i:
            return i
        if "url" in i:
            return i
        if "URL" in i:
            return i

'''def get_telephone_numb(text):
    #print "HT"
    for i in text:
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








'''def get_fax_numb(text):
    print len("Himanshu")
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




def get_email_id(text):
    for i in text:
        if("Email:" in i):
            return i
        if("EMAIL:" in i):
            return i
        if("@" in i):
            return i

def get_address(text):
    str="〒"
    for i in text:
        if str in i:
            return i


def get_mobile_number(text):
    for i in text:
        if "携帯:" in i:
            return i 
        if "Mobile:" in i:
            return i
        if "MOBILE:" in i:
            return i

def extract_entities(text):

    url = 'https://language.googleapis.com/v1beta1/documents:analyzeEntities?key=API KEY HERE'
    header = {'Content-Type': 'application/json'}
    body = {
        "document": {
            "type": "PLAIN_TEXT",
            "language": "JA",
            "content": text
        },
        "encodingType": "UTF8"
    }
    response = requests.post(url, headers=header, json=body).json()
    #print response
    return response
                


def extract_required_entities(text):
    entities = extract_entities(text)
    required_entities = {'ORGANIZATION': '', 'PERSON': '', 'LOCATION': '','NUMBER': ''}
    for entity in entities['entities']:
        t = entity['type']
        if t in required_entities:
            required_entities[t] += entity['name']
    #print required_entities
    return required_entities


'''def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)'''


if __name__ == '__main__':
    extracted_text=detect_text("FILE PATH HERE")
    my_data= extract_required_entities(extracted_text)
    #str='\u30b3\u30bd\u30dc\u5171\u548c\u56fd\u5927\u4f7f\u9928'
    #print u'\u30b3\u30bd\u30dc\u5171\u548c\u56fd\u5927\u4f7f\u9928'
    #print("here is your checkmark: " + u'\u2713');
    print "-----------------------------------------"
    #print my_data
    print my_data['PERSON']
    #print my_data['ORGANIZATION']

    #print my_data['NUMBER']
    #print my_data['LOCATION']
    #str1=unicode(str,'utf_8')
    #print "HT",str1
    ##print str2
    copy=extracted_text.split('\n')
    ans=get_company_name(copy)
    if ans==None:
        ans=my_data['ORGANIZATION']
    print "Company Name - ",ans
    copy1=extracted_text.split()
    #print copy
    tel_numb=get_telephone_numb(copy)
    print "Tel No- ",tel_numb

    #mob_numb=get_mobile_number(copy)
    #print mob_numb

    fax_numb=get_fax_numb(copy)
    print "FAX No- ",fax_numb

    email_id=get_email_id(copy)
    print email_id

    web_address=get_web_address(copy)
    print web_address

    address=get_address(copy)
    print address


    #print get_human_names(extracted_text)