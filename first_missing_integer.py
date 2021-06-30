#First Missing Integer
#Problem Description
#
#Given an unsorted integer array A of size N. Find the first missing positive integer.
#
#Note: Your algorithm should run in O(n) time and use constant space.
#
#
#
#Problem Constraints
#1 <= N <= 1000000
#
#-109 <= A[i] <= 109
#
#
#
#Input Format
#First argument is an integer array A.
#
#
#
#Output Format
#Return an integer denoting the first missing positive integer.

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        hashA={}
        for i in A:
            if hashA.get(i):
                hashA[i]+=1
            else:
                hashA[i]=1
        for j in range(1,10**6+1):
            if hashA.get(j):
                continue
            else:
                return j
        return -1
