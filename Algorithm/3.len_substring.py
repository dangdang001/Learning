# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:12:57 2017

@author: dyin
"""


class Solution(object):
    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        def IfNoDup(str):
            if len(''.join(set(str)))==len(str):
                return True
            else:
                return False
        string_now=""
        max_len=0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                string_now=s[i:j]
                if IfNoDup(string_now):
                    if len(string_now)>max_len:
                        max_len=len(string_now)
        return(max_len)
    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        def IfNoDup(str):
            if len(''.join(set(str)))==len(str):
                return True
            else:
                return False
        string_now=""
        max_len=0
        i=0
        j=0
        while i<len(s) & j<len(s):
                if s[j] not in string_now:
                    string_now+=s[j]
                    if len(string_now)>max_len:
                        max_len=len(string_now)
                    j+=1
                else:
                    string_now=""
                    i+=1
        return(max_len)
Solution().lengthOfLongestSubstring1(s="abcdaef")
Solution().lengthOfLongestSubstring2(s="abcdaef")