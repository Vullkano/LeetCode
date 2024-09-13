class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index1 = 0
        for i in haystack:
            if i == needle[0]:
                index = 1
                while haystack[index1:index1+index] == needle[0:index]:
                    if haystack[index1:index1+index] == needle:
                        return index1
                    index += 1
            index1 += 1
        return -1