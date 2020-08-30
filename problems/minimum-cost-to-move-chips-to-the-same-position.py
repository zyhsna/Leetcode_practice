class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        return min(sum(1 for i in position if i%2==1),sum(1 for i in position if i%2==0))