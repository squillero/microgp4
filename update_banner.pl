#!/usr/bin/env perl -w-

use utf8;
undef $/;

$old = <<'OLD';
#############################################################################\s*
#          __________                                                       #\s*
#   __  __/ ____/ __ \\__ __   This file is part of MicroGP4.*#\s*
#  / / / / / __/ /_/ / // /   \(!\) by Giovanni Squillero and Alberto Tonda   #\s*
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #\s*
# \\__  /\\____/_/   /__  __/                                                 #\s*
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!" #\s*
#                                                                           #\s*
#############################################################################\s*
OLD

$new = <<'NEW';
#############################################################################
#          __________                                                       #
#   __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0a1 "Kiwi"   #
#  / / / / / __/ /_/ / // /   A versatile evolutionary optimizer & fuzzer   #
# / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4         #
# \__  /\____/_/   /__  __/                                                 #
#   /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!"  #
#                                                                           #
#############################################################################

NEW

foreach $f (@ARGV) { 
    open FILE, $f or die "Yeuch. Can't open $f:\n\t$!";
    $_ = <FILE>;
    close FILE;

    s|$old|$new|gs;

    open FILE, ">$f" or die "Yeuch. Can't open $f:\n\t$!";
    print FILE "$_";
    close FILE;
}
