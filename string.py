"""
Returns the cost to make a string p from a given string s


	Cost to append a new character is 1
	No cost to append a substring of p

"""



def stringConstruction(s):			#'s' is the test string
    
    price=0
    x=''
    c=0

    L=range(0,len(s))
    for i in L:

        
        if i==1:
        
            x+=s[i]
            price+=1
            
        else:
            
            if s[i] not in s[:i]:
                x+=s[i]
                price+=1
                
            else:
                
                for j in range(i,len(s)):

                    if i==len(s)-1:

                        x+=s[i]
                    
                    
                    elif s[s.find(s[j])]==s[s.find(s[j+1])]:
                        c+=1
                        continue
                        
                    else:
                        
                        if c!=0:
                            
                            x+=s[i:j]
                            del L[i:j+1]
                            break
                            
                            
                        else:
                            
                            break
    return price
