#Find a peak element
#Problem Description
#
#Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors.
#
#For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
#
#NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
#Problem Constraints
#1 <= |A| <= 100000
#
#1 <= A[i] <= 109
#
#
#
#Input Format
#The only argument given is the integer array A.
#
#
#
#Output Format
#Return the peak element.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def BS(a,l,r):
            mid=(l+r)//2
            if a[mid]>=a[mid-1] and a[mid]>=a[mid+1]:
                return a[mid]
            else:
                if a[mid]>=a[mid-1]:
                    return BS(a,mid+1,r)
                else:
                    return BS(a,l,mid-1)
        if len(A)==1:
            return A[0]
        elif A[1]<A[0]:
            return A[0]
        elif A[len(A)-1]>A[len(A)-2]:
            return A[len(A)-1]
        else:
            return BS(A,0,len(A)-1)
                
            
