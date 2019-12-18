# Implement pow(x, n), which calculates x raised to the power n (xn).

class Solution:
    def myPow(self, x, n):

TBD:
class Solution {
public:
    
    double qpow(double a, long long b){
        double res = 1;
        while(b){
            if(b&1) res = res*a;
            b >>= 1;
            a *= a;
        }
        return res;
    }
    
    
    double myPow(double x, long long n) {
        if(n == 0) return 1;
        if(n > 0) return qpow(x,n);
        if(n < 0) return 1/qpow(x,-n);
        return 1.0;
    }
};

作者：0x404
链接：https://leetcode-cn.com/problems/powx-n/solution/ji-bai-cbai-fen-bai-yong-hu-by-0x404/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。