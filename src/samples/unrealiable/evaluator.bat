@echo off

rem echo ciao >&2 

set PATH=%PATH%;C:\Program Files\Git\usr\bin\

cat %1 | wc -l
cat %1 | wc -w
cat %1 | wc -c

