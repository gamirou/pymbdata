@echo off

set /p script=What example do you want to run?

py examples\%script%Example.py
pause