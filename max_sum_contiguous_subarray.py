#Max Sum Contiguous Subarray
#Problem Description
#
#Find the contiguous subarray within an array, A of length N which has the largest sum.
#
#
#
#Problem Constraints
#1 <= N <= 1e6
#-1000 <= A[i] <= 1000
#
#
#
#Input Format
#The first and the only argument contains an integer array, A.
#
#
#
#Output Format
#Return an integer representing the maximum possible sum of the contiguous subarray.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        glob=A[0]
        curr=A[0]
        for j in range(1,len(A)):
            curr=max(A[j],A[j]+curr)
            if curr>glob:
                glob=curr
        return glob