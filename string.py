def stringConstruction(s):

    cost=0
    p=''
    t=0

    L=range(0,len(s))
    for i in L:

        
        if i==1:
        
            p+=s[i]
            cost+=1
        elif i==2:
            p+=s[i+1]
            cost+=2
        else:
            
            if s[i] not in s[:i]:			#new character
                p+=s[i]
                cost=cost+1
          

            else:
                
                for j in range(i,len(s)):

                    if i==len(s)-1:

                        p+=s[i]
                    
                    
                    elif s[s.find(s[j])]==s[s.find(s[j+1])]:                     #finding substrings 
                        t+=1
                        continue
                        
                    else:
                        
                        if t!=0:
                            
                            p+=s[i:j]
                            del L[i:j+1]                                         #removing already added cases
                            break
                            
                            
                        else:
                            
                            break
    print "the cost to  make the new string is:",cost
    return cost
