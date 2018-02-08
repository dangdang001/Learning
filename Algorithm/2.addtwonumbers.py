# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 15:00:29 2017

@author: dyin

Leetcode Problem 2: Add two numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

"""

class ListNode(object):
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        carry, current=0, dummy
        while l1 or l2:
            val=carry
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            carry=val / 10
            val=val % 10
            current.next=ListNode(val)
            current=current.next
        # Check if the sum have an extra carry of one at the end
        if carry == 1:
            current.next=ListNode(1)
        return dummy.next

if __name__=="__main__":
    a, a.next, a.next.next=ListNode(2), ListNode(4),ListNode(3)
    b, b.next, b.next.next=ListNode(5), ListNode(6),ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print "{0}->{1}->{2}".format(result.val, result.next.val, result.next.next.val)
        
    
