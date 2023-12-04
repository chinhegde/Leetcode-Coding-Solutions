class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(1,len(digits)+1):
            if c==1:
                digits[-i]+=1
            else:
                break
                
            if digits[-i]>9:
                digits[-i]=0
            else:
                c=0
        if digits[0] == 0:
            digits.insert(0,1)
        return digits
                