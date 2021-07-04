#Delete Elements
#Problem Description
#
#Given an integer array A of size N.
#Find the minimum number of elements that need to be removed such that the GCD of the resulting array becomes 1.
#
#If not possible then return -1.
#
#
#
#Problem Constraints
#1 <= N <= 100000
#1 <= A[i] <= 1e9
#
#
#Input Format
#Input contains a single integer array A
#
#
#
#Output Format
#Return an integer
#
#
#
#Example Input
#Input 1:
#
# A = [7, 2, 5]
#
#
#Example Output
#Output 1:
#
# 0
#
#
#Example Explanation
#Explanation 1:
#
# GCD of the array A is 1.
# so, the number of elements to be removed is 0.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        def gcd(a,b):
            a,b=abs(a),abs(b)
            if b==0:
                return a
            return gcd(b,a%b)
        if A[0]==1:
            return 0
        ps_gcd=[A[0]]
        for i in range(1,len(A)):
            ps_gcd.append(gcd(ps_gcd[i-1],A[i]))
            if ps_gcd[-1]==1:
                return 0
        return -1
            
