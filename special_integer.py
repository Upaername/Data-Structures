#Special Integer
#Problem Description
#
#Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B.
#
#
#
#Problem Constraints
#1 <= |A| <= 100000
#1 <= A[i] <= 10^9
#
#1 <= B <= 10^9
#
#
#
#Input Format
#The first argument given is the integer array A.
#
#The second argument given is integer B.
#
#
#
#Output Format
#Return the maximum value of K (sub array length).

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self,A, B):
        pre_a=[]
        sum=0
        for i in A:
            sum+=i
            pre_a.append(sum)
        def ps_sum(A,l,r):
            if l-1<0:
                return A[r]
            return A[r]-A[l-1]
        def check_subarrays(A,num):
            i=0
            ans=0
            while i+num-1<=len(A)-1:
                ans=max(ans,ps_sum(A,i,i+num-1))
                i+=1
            return ans
        def BS(a,l,r,B):
            mid=(l+r)//2
            if l==r or r==l+1:
                if check_subarrays(a,r)<=B:
                    return r
                else:
                    return l
            else:
                if check_subarrays(a,mid)<=B:
                    return BS(a,mid,r,B)
                else:
                    return BS(a,l,mid-1,B)
        return BS(pre_a,1,len(A),B)