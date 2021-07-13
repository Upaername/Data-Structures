#Sorted Insert Position
#Problem Description
#
#Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
#If not, return the index where it would be if it were inserted in order.
#
#NOTE: You may assume no duplicates in the array. Users are expected to solve this in O(log(N)) time.
#
#
#
#Problem Constraints
#1 <= N <= 106
#
#
#
#Input Format
#First argument is an integer array A of size N.
#Second argument is an integer B.
#
#
#
#Output Format
#Return an integer denoting the index of target value.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        if len(A)==1 and B>A[0]:
            return 1
        elif len(A)==1 and B<A[0]:
            return 0
        # count=0
        def BS(a,l,r,B):
            mid=(l+r)//2
            if a[mid]==B:
                return mid
            elif (r==l or r==l+1) and B!=a[l] and B!=A[r]:
                if B>a[l] and B<a[r]:
                    return l+1
                elif B>a[r]:
                    return r+1
                elif B<a[l]:
                    return l
            else:
                if a[mid]>B:
                    return BS(a,l,mid-1,B)
                else:
                    return BS(a,mid+1,r,B)
        return BS(A,0,len(A)-1,B)
        
