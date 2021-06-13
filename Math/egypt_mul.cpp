#include <cstdio>
using namespace std;

bool odd(int n) { return n & 1; }
int half(int n) { return n >> 1; }

//朴素, O(n)
int mul0(int n, int a) {
    if (n == 1) return a;
    return mul0(n-1, a) + a;
}

//O(logn), 递归调用开销
int mul1(int n, int a) {
    if (n == 1) return a;
    int result = mul1(half(n), a + a);
    if (odd(n)) result += a;
    return result;
}

//invirant: r + na = r0 + n0*a0
//add remainder, transform to tail recursion
int mul_acc1(int r, int n, int a) {
    if (n == 1) return r + a;
    if (odd(n)) r += a;
    return mul_acc1(r, half(n), a + a);
}

//optimize if condition
int mul_acc2(int r, int n, int a) {
    if (odd(n)) {
        if (n == 1) return r + a;
        r += a;
    }
    return mul_acc2(r, half(n), a + a);
}

int mul_acc3(int r, int n, int a) {
    if (odd(n)) {
        if (n == 1) return r + a;
        r += a;
    }
    n = half(n);
    a = a + a;
    return mul_acc2(r, n, a);
}

int main() {
    printf("mul0(7,8) = %d\n", mul0(7,8));
    printf("mul1(7,8) = %d\n", mul1(7,8));
    return 0;
}


