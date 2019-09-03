def anagram(string1,string2):
    
    string1=string1.replace(' ','').lower()
    string2=string2.replace(' ','').lower()
    
    return sorted(string1) == sorted(string2)


string1 = input('Enter first word :\n')
string2 = input('Enter second word :\n')

res = anagram(string1,string2)

if res == True:
    print("Given words are Anagram")
else:
    print("Given words are not Anagram")