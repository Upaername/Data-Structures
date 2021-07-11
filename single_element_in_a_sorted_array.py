#Single Element in a Sorted Array
#Problem Description
#
#Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.
#
#NOTE: Users are expected to solve this in O(log(N)) time.
#
#
#
#Problem Constraints
#1 <= |A| <= 100000
#
#1 <= A[i] <= 10^9
#
#
#
#Input Format
#The only argument given is the integer array A.
#
#
#
#Output Format
#Return the s

class Solution:
    # @param A : list of integers
    # @return an integer

    def solve(self,A):
        def BS(a, l, r):
    #         mid=l+r//2
            if l>r:
                return -1
            elif l==r:
                # print("A[l]",A[l])
                return A[l]
            else:
                mid=(l+r)//2
                # print("l",l)
                # print("r",r)
                if mid&1==0:
                    # print(mid)
                    if A[mid]==A[mid+1]:
                        return BS(a,mid+2,r)
                    elif A[mid]==A[mid-1]:
                        return BS(a,l,mid-2)
                    else:
                        return A[mid]
                else:
                    # print(mid)
                    if A[mid]==A[mid-1]:
                        return BS(a,mid+1,r)
                    elif A[mid]==A[mid+1]:
                        return BS(a,l,mid-1)
                    else:
                        return A[mid]
        return BS(A,0,len(A)-1)