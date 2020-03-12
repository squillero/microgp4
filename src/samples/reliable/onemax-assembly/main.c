/***************************************************************************\
*          __________                                                       *
*   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0 "Kiwi"     *
*  / / / / / __/ /_/ / // /   (!) by Giovanni Squillero and Alberto Tonda   *
* / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         *
* \__  /\____/_/   /__  __/                                                 *
*   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!" *
*                                                                           *
\***************************************************************************/

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
