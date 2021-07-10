#Sorted Permutation Rank with Repeats
#Problem Description
#
#Given a string A, find the rank of the string amongst its permutations sorted lexicographically. Note that the characters might be repeated. If the characters are repeated, we need to look at the rank in unique permutations. Look at the example for more details.
#
#NOTE:
#
#The answer might not fit in an integer, so return your answer % 1000003 where 1000003 is a prime number.
#String A can consist of both lowercase and uppercase letters. Characters with lesser ascii value are considered smaller i.e. 'a' > 'Z'.
#
#
#Problem Constraints
#1 <= len(A) <= 1000000
#
#
#
#Input Format
#First argument is a string A.
#
#
#
#Output Format
#Return an integer denoting the rank.


from operator import mul
from functools import reduce
from itertools import permutations, takewhile
from collections import Counter
class Solution:
    # @param A : string
    # @return an integer
#     @profile
    def findRank(self, A):
        A = tuple(A)
        Al = sorted(A)
        lena = len(A)
        freq = Counter(A)
        facts = [1]
        for i in range(1, lena+1):
            facts.append(facts[-1]*i%1000003)
        freq_fact = reduce(mul, [facts[x] for x in freq.values()])%1000003
        prev = set(takewhile(lambda x: ord(x) < ord(A[0]), Al))
        prev_rank = 1
        for p in prev:
            prev_rank += facts[lena-1]*freq[p]%1000003*pow(freq_fact, 1000001, 1000003)
        for i in range(lena-2):
            A_s = A[i+1:]
            c = A_s[0]
            Al_s = sorted(A_s)
            prev_s = set(takewhile(lambda x: x < c, Al_s))
            if not prev_s:
                continue
            freq_s = Counter(A_s)
            freq_fact_s = reduce(mul, [facts[x] for x in freq_s.values()])%1000003
            for p in prev_s:
                a = facts[lena-i-2]*freq_s[p]%1000003
                b = pow(freq_fact_s, 1000001, 1000003)
                prev_rank += a*b
        return prev_rank%1000003