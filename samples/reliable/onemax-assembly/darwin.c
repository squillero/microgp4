/***************************************************************************\
*          __________                                                       *
*   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   *
*  / / / / / __/ /_/ / // /   A versatile evolutionary optimizer & fuzzer   *
* / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         *
* \__  /\____/_/   /__  __/                                                 *
*   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!"  *
*                                                                           *
\***************************************************************************/

// skeleton for the instruction library
// compile it with "gcc -S -c" and look at the prologue

#include <stdio.h>
#include <stdlib.h>

int darwin()
{
    int var = 1;
    var = 22*var;
    return var;
}
