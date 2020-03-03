/*-**********************************************************************-*\
*             * CLASS SAMPLE FOR "COMPUTER SCIENCES" (04JCJ**)             *
*   #####     * (!) 2020, Giovanni Squillero <squillero@polito.it>         *
*  ######     *                                                            *
*  ###   \    * Copying and distributing this file, either with or without *
*   ##G  c\   * modification, is permitted in any medium without royalty,  *
*   #     _\  * provided that this 10-line comment is preserved.           *
*   |  _/     *                                                            *
*             * ===> THIS FILE IS OFFERED AS-IS, WITHOUT ANY WARRANTY <=== *
\*-**********************************************************************-*/

#include <stdio.h>
#include <stdlib.h>

int darwin();

int main(int argc, char *argv[])
{
    unsigned int x = darwin();

    int n = 0;
    while(x) {
        n += x & 0x1;
        x >>= 1;
    }
    printf("%d\n", n);
    return EXIT_SUCCESS;
}
