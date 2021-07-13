#Single Number III
#Problem Description
#
#Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
#Note: Output array must be sorted.
#
#
#
#Problem Constraints
#2 <= |A| <= 100000
#1 <= A[i] <= 109
#
#
#
#Input Format
#First argument is an array of interger of size N.
#
#
#
#Output Format
#Return an array of two integers that appear only once.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor=0
        for i in A:
            xor^=i
        bit=-1
        for i in range(32):
            if 1<<i & xor:
                bit=i
                break
        c=0
        d=0
        for i in A:
            if (1<<bit & i)==0:
                c^=i
            else:
                d^=i
        return sorted([c,d])
                
                
