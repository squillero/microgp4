@echo off

rem commenti utili & inutili

del a.exe
gcc main.o %1

if exist a.exe (
    .\a.exe
) else (
    echo -1
)
