python -m pip install --upgrade pip


@ECHO OFF
python check_python_version.py > output
SET /p VERSION=<output
ECHO %VERSION%
IF "%VERSION%" == "3.5" (
	python download_binaries.py
	pip install qtpy pyqtgraph scikit-image xmltodict ipython zmq ipykernel qtconsole pyopengl nd2reader tifffile openpyxl
	python download_flika.py
	python flika/flika.py
) ELSE (
	ECHO This install script requires Python 3.5. Your version of python is %VERSION%. Flika install Failed.
)


