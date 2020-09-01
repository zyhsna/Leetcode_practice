class Solution:
    def commonChars(self, A):
        from collections import Counter
        ans = Counter(A[0])
        for i in A[1:]:
            ans &= Counter(i)
        return list(ans.elements())