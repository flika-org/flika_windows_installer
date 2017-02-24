python -m pip install --upgrade pip


@ECHO OFF
python check_python_version.py > output
SET /p VERSION=<output
ECHO %VERSION%
IF "%VERSION%" == "3.5" (
	pip install "binary_dependencies/numpy-1.12.0+mkl-cp35-cp35m-win_amd64.whl"
	pip install binary_dependencies/scipy-0.19.0rc2-cp35-cp35m-win_amd64.whl
	pip install binary_dependencies/PyQt4-4.11.4-cp35-cp35m-win_amd64.whl
	pip install qtpy pyqtgraph scikit-image xmltodict ipython zmq ipykernel qtconsole pyopengl nd2reader tifffile openpyxl
	python download_flika.py
	python flika/flika.py
) ELSE (
	ECHO This install script requires Python 3.5. Your version of python is %VERSION%. Flika install Failed.
)


