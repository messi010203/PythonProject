#coding:utf-8

def pigLatin(centences):
    '''
    拉丁猪文字游戏
    基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并且加上后缀-ay（譬如“banana”会变成“anana-bay”
    '''
    def getWordIndex(word):
        index=0
        for w in word:
            if index==0 and word[index].lower() not in 'aeiou':
                index+=1
            else:
                if index>=0 and word[index].lower() not in 'aeiou':
                    index+=1
                else:
                    break
        return index
    
    wds=centences.split(' ')
    newwds=[]
    for w in wds:
        wdindex= getWordIndex(w)
        if wdindex==0:
            w=w+'-hay'
        else:
            w=w[wdindex:len(w)]+'-'+w[0:wdindex]+'ay'
        newwds.append(w)
        
    return ' '.join(newwds)
    
    return wds
    
print pigLatin('Welcome to the Python world Are you ready')
