@echo off

rem comment

del a.exe
gcc main.o %1

if exist a.exe (
    .\a.exe
) else (
    echo -1
)
