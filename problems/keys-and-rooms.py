# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/31 17:45
# 文件名：keys-and-rooms.py
# 开发工具：PyCharm
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        lockedroom = set(range(1, len(rooms)))
        keys = set(rooms[0])
        while len(keys) != 0:
            newkeys = set()
            for k in keys:
                if k not in lockedroom:
                    continue
                lockedroom.remove(k)
                for nk in rooms[k]:
                    if nk in lockedroom:
                        newkeys.add(nk)
            keys = newkeys
        return len(lockedroom==0)