class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        

        for i in nums:
            if i in d.keys():
                d[i] += 1
              
                    
            else:
                d[i] = 1

        top_item = [x[0] for x in sorted(d.items(), key=lambda x: x[1], reverse=True)[:k]]
        return top_item

        
                
                
                

        return list(l)