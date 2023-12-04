class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = list(num1[::-1])
        num2 = list(num2[::-1])

        if len(num1) > len(num2): num2 = num2 + ['0']*(len(num1) - len(num2))
        elif len(num1) < len(num2): num1 = num1 + ['0']*(len(num2) - len(num1))

        i = 0
        c = 0

        res = list()

        while i<len(num1):
            s = c+(ord(num2.pop(0))+ord(num1.pop(0)))%48
            if s >= 10: 
                c = 1
                s = s%10
            else:
                c = 0
            res.append(str(s))
        if c == 1:
            res.append('1')
        return ''.join(res[::-1])







