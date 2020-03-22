@echo off

rem **************************************************************************
rem           __________                                                      
rem    __  __/ ____/ __ \__ __   This file is part of MicroGP4 v1.0 "Kiwi"    
rem   / / / / / __/ /_/ / // /   (!) by Giovanni Squillero and Alberto Tonda  
rem  / /_/ / /_/ / ____/ // /_   https://github.com/squillero/microgp4        
rem  \__  /\____/_/   /__  __/                                                
rem    /_/ --MicroGP4-- /_/      "You don't need a big goal, be μ-ambitious!!"
rem                                                                           
rem **************************************************************************

echo 42
exit 0

del a.exe
gcc main.c %1

if exist a.exe (
    .\a.exe
) else (
    echo -1
)
