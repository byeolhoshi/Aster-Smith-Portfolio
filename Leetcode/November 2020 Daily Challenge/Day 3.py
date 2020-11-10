"""
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

"""

class Solution:
    def maxPower(self, s: str) -> int:
        power = []
        count = 1
        
        if len(s) == 1: 
            return 1
        
                

        for i in range(0, len(s)-1):
            
            if(s[0] != None):
                power.append(count)
                
            if s[i] == s[i+1]: 
                count+=1
                
                
            else: 
                power.append(count)
                count = 1
        power.append(count)
                
        if len(power) == 0:
            return None
        else: 
            return max(power)
            
            
            
 """ 
 o(n) run time worst case, o(1) best case 
 
 48 ms run time solution
 
 """
