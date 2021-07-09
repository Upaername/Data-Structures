
#Single Number
#Problem Description
#
#Given an array of integers A, every element appears twice except for one. Find that single one.
#
#NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
#
#
#Problem Constraints
#2 <= |A| <= 2000000
#
#0 <= A[i] <= INTMAX
#
#
#
#Input Format
#First and only argument of input contains an integer array A.
#
#
#
#Output Format
#Return a single integer denoting the single element.


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans=A[0]
        for i in range(1,len(A)):
            ans^=A[i]
        return ans
            