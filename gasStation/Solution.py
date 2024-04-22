class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return an integer
	def canCompleteCircuit(self, A, B):
		if (sum(A) < sum(B)):
			return -1
		min_sum, min_index, total = 0, 0, 0
        for i in range(len(A)):
            total += A[i] - B[i]
            if min_sum > total:
                min_sum, min_index = total, i + 1
        return -1 if total < 0 else min_index
