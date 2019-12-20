class Solution:
    def largestPerimeter(self, A):
        A.sort()
        A = A[::-1] # decending order of A

        for i in range(len(A)):
            a, b, c = A[i], A[i+1], A[i+2]
            if a+b>c and a+c>b and b+c>a:
                return (A[i] + A[i+1] + A[i+2])
            if i+2 == len(A)-1:
                return 0