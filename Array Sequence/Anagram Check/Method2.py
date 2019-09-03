def anagram(string1,string2):
    
    string1=string1.replace(' ','').lower()
    string2=string2.replace(' ','').lower()
    
    #check length
    if len(string1) != len(string2):
        return False
    
    count = {}
    
    for letter in string1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
            
    for letter in string2:
        if letter in count:
            count[letter] -= 1
        else: 
            count[letter] = 1
            
    for ele in count:
        if count[ele] != 0:
            return False
        
    
    return True
    