#include <stdio.h>
#include <stdlib.h>

int x = 1, y = 2, z[10];
int ip;
ip = &x;
y = *ip;
*ip = 0;
ip = &z[0];

printf("x = %d \n y = $d \n ip = %d\n *ip = %d", x, y, ip, *ip);



