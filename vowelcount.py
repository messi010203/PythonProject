#coding:utf-8


def getVowelCount(string):
    dic={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in string:
    	i=i.lower()
        if i in dic:
            dic[i]+=1
             
    return dic     


dic= getVowelCount('Welcome to the Python world Are you ready')
for key in dic:
    print key,dic[key]
