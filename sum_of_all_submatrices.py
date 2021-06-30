#Sum of all Submatrices
#Problem Description
#
#Given a 2D Matrix A of dimensions N*N, we need to return sum of all possible submatrices.
#
#
#
#Problem Constraints
#1 <= N <=30
#
#0 <= A[i][j] <= 10
#
#
#
#Input Format
#Single argument representing a 2-D array A of size N x N.
#
#
#
#Output Format
#Return an integer denoting the sum of all possible submatrices in the given matrix.

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        ans=0
        for i in range(len(A)):
            for j in range(len(A)):
                ans+=A[i][j]*(i+1)*(j+1)*(len(A)-i)*(len(A)-j)
        return ans
            
