#Kth Smallest Element
#Problem Description
#
#Find the Bth smallest element in given array A .
#
#NOTE: Users should try to solve it in <= B swaps.
#
#
#
#Problem Constraints
#1 <= |A| <= 100000
#
#1 <= B <= min(|A|, 500)
#
#1 <= A[i] <= 109
#
#
#
#Input Format
#First argument is vector A.
#
#Second argument is integer B.
#
#
#
#Output Format
#Return the Bth smallest element in given array.
#
#
#
#Example Input
#Input 1:
#
#A = [2, 1, 4, 3, 2]
#B = 3
#Input 2:
#
#A = [1, 2]
#B = 2
#
#
#Example Output
#Output 1:
#
# 2
#Output 2:
#
# 2
#
#
#Example Explanation
#Explanation 1:
#
# 3rd element after sorting is 2.
#Explanation 2:
#
# 2nd element after sorting is 2.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        A=list(A)
        # print(A.sort()[8])
        def swap(A,l,r):
            temp=A[l]
            A[l]=A[r]
            A[r]=temp
            return A
        for i in range(B):
            mini=1000000000
            mini_i=None
            for j in range(i+1,len(A)):
                if A[j]<A[i] and A[j]<mini:
                    mini=A[j]
                    mini_i=j
                    
                else:
                    pass
            if mini_i:
                swap(A,i,mini_i)
            else:
                pass
        return A[B-1]