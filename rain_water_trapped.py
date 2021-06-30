#Rain Water Trapped

#Problem Description
#
#Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#Problem Constraints
#1 <= |A| <= 100000
#
#Input Format
#First and only argument is the vector A
#
#Output Format
#Return one integer, the answer to the question

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        pre_a=[A[0]]
        for i in range(1,len(A)):
            temp=max(pre_a[i-1],A[i])
            pre_a.append(temp)
        post_a=[A[-1]]
        for j in range(len(A)-2,-1,-1):
            temp=max(post_a[len(A)-j-2],A[j])
            post_a.append(temp)
        post_a=post_a[::-1]
        ans=0
        for i in range(len(A)):
            if i-1<0:
                left=0
            else:
                left=pre_a[i-1]
            if i+1>=len(A):
                right=0
            else:
                right=post_a[i+1]
            if left>A[i] and right>A[i]:
                ans=ans+(min(left,right)-A[i])
        return ans
            
