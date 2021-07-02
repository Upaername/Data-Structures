#Sum the Difference
#Problem Description
#
#Given an integer array A of size N.
#You have to find all possible non-empty subsequence of the array of numbers and then, for each subsequence, find the difference between the largest and smallest numbers in that subsequence Then add up all the differences to get the number.
#
#As the number may be large, output the number modulo 1e9 + 7 (1000000007).
#
#NOTE: Subsequence can be non-contiguous.
#
#
#
#Problem Constraints
#1 <= N <= 10000
#
#1<= A[i] <=1000
#
#
#
#Input Format
#First argument is an integer array A.
#
#
#
#Output Format
#Return an integer denoting the output.

def solve(self, A):
    MOD=1000000007
    A.sort()
     
    # iterate over array and with help of
    # horner's rule calc max_sum and min_sum
    min_sum = 0
    max_sum = 0
    n=len(A)
    for i in range(0,n):
        max_sum = 2 * max_sum + A[n-1-i]
        max_sum %= MOD
        min_sum = 2 * min_sum + A[i]
        min_sum %= MOD
     
    return (max_sum - min_sum) % MOD
	

