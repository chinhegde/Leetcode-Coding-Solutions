# https://leetcode.com/problems/defanging-an-ip-address/description/
# 1108. Defanging an IP address

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        