#Rotated Sorted Array Search
#Problem Description
#
#Given a sorted array of integers A of size N and an integer B.
#
#array A is rotated at some pivot unknown to you beforehand.
#
#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
#
#You are given a target value B to search. If found in the array, return its index, otherwise return -1.
#
#You may assume no duplicate exists in the array.
#
#NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
#Problem Constraints
#1 <= N <= 1000000
#
#1 <= A[i] <= 10^9
#
#all elements in A are disitinct.
#
#
#
#Input Format
#The first argument given is the integer array A.
#
#The second argument given is the integer B.
#
#
#
#Output Format
#Return index of B in array A, otherwise return -1

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        if len(A)==1 and A[0]==B:
            return 0 
        def BS(a,l,r):
            mid=(l+r)//2
            if a[mid]<a[mid+1] and a[mid]<a[mid-1]:
                return mid
            elif a[mid]>a[-1]:
                return BS(a,mid+1,r)
            elif a[mid]<a[-1]:
                return BS(a,l,mid-1)
        mid=BS(A,0,len(A)-1)
        
        def BS1(a,l,r,k):
            mid=(l+r)//2
            if a[mid]==k:
                return mid
            elif a[mid]>k:
                return BS1(a,l,mid-1,k)
            else:
                return BS1(a,mid+1,r,k)
        try:        
            if B==A[mid]:
                return mid
            elif B>A[mid] and B<A[-1]:
                return BS1(A,mid+1,len(A)-1,B)
            elif B>A[mid] and B>A[-1]:
                return BS1(A,0,mid-1,B)
        except:
            return -1