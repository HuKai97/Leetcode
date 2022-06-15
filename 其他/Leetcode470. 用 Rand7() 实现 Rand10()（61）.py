# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        index = float('inf')
        while index >= 40:
            # 超过40的话就重新选
            index = 7 * (rand7() - 1) + (rand7() - 1)
        return index % 10 + 1