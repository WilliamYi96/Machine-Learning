# Implement pow(x, n), which calculates x raised to the power n (xn).

# class Solution:
#     def myPow(self, x, n):

# TBD:
# class Solution {
# public:
    
#     double qpow(double a, long long b){
#         double res = 1;
#         while(b){
#             if(b&1) res = res*a;
#             b >>= 1;
#             a *= a;
#         }
#         return res;
#     }
    
    
#     double myPow(double x, long long n) {
#         if(n == 0) return 1;
#         if(n > 0) return qpow(x,n);
#         if(n < 0) return 1/qpow(x,-n);
#         return 1.0;
#     }
# };

class Solution:
    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        half = self.fastPow(x, n / 2)
        print(half, n)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    def myPow(self, x, n):
        N = n 
        if N < 0:
            N = -N 
            x = 1 / x
        print("x, N = {}, {}".format(x, N))
        return self.fastPow(x, N)

# There is some problems of this file.