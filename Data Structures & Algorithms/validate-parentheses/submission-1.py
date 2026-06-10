class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for c in s:
            if c in {'(','{','['}:
                l.append(c)
            elif c==')':
                if len(l)>0 and l[-1]=='(':
                    l.pop()
                else:
                    return False
            elif c=='}':
                if len(l)>0 and l[-1]=='{':
                    l.pop()
                else:
                    return False
            elif c==']':
                if len(l)>0 and l[-1]=='[':
                    l.pop()
                else:
                    return False
        
        if len(l)>0:
            return False
        else:
            return True
            
