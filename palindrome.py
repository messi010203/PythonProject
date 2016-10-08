#coding:utf-8

 

def palindrome(string):
    tmp_str = str(string).strip()
    highindex = len(tmp_str) - 1  
    lowindex = 0  
    while highindex > lowindex:
        if tmp_str[highindex] == tmp_str[lowindex] :  
            highindex -= 1   
            lowindex += 1  
            continue  
        else :   
            return False  
    return True

def is_palindrome(n):  
    n=str(n)  
    m=n[::-1]  
    return n==m 

string='asd2dsa'
print is_palindrome(string)
print palindrome(string)