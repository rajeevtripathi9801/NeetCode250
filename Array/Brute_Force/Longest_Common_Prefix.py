from typing import List 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for counter in range(0, len(strs[0])):
            for s in strs:
                if counter == len(s) or s[counter] != strs[0][counter]:
                    return res
            
            res = res + strs[0][counter]
        
        return res

if __name__=="__main__":
    obj = Solution()
    s = ["flower", "flow", "flight"]
    res = obj.longestCommonPrefix(s)
    print(res)                      # fl in this case 

""" 
One thing about strs[0][counter] means -> go to 0 element of list strs and then access the counter valued
index there


example:- ["flow", "flower", "fligh"] current = 2
Here strs[1][current] means acess the first word of the string then 2 cahracter oif the string. 

In memory they are stored sequentially."""