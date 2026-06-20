class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            l1= [i for i in s]
            l2= [i for i in t]
            if sorted(l1)==sorted(l2):
                return True
            else:
                return False