#include <stdio.h>

int main() {
    int a[4] = {1,2,3,4};
    int *p = a;
    printf("    a=%p\n   &a=%p\n&a[0]=%p\n", a, &a, &a[0]);
    printf("    p=%p\n   &p=%p\n&p[0]=%p\n", p, &p, &p[0]);
    return 0;
}

