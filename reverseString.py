def reverseString(string):
#     string=string[::-1] #first method
    string=reversed(string) #second method
    return ''.join(string)
    

print reverseString('123')
