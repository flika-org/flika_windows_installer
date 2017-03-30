python -m pip install --upgrade pip


@ECHO OFF
python check_python_version.py > python_version.txt
SET /p VERSION=<python_version.txt
ECHO %VERSION%
IF "%VERSION%" == "3.5" GOTO download_binaries
IF "%VERSION%" == "3.6" GOTO download_binaries
ECHO This install script requires Python 3.5 or 3.6. Your version of python is %VERSION%. Flika install Failed.



:download_binaries
python download_binaries.py
pip install flika
flika
:end