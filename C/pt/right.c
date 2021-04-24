#include <stdio.h>

int main() {
    extern char *p;
    extern char a[];
    printf("p[3]=%c\n", p[3]);
    printf("a[3]=%c\n", a[3]);
    return 0;
}
