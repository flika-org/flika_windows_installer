from urllib.request import urlretrieve
import os, sys
import pip


numpy_fn  = "numpy-1.12.0+mkl-cp35-cp35m-win_amd64.whl"
scipy_fn  = "scipy-0.19.0rc2-cp35-cp35m-win_amd64.whl"
pyqt4_fn = "PyQt4-4.11.4-cp35-cp35m-win_amd64.whl"
names = ['numpy', 'scipy', 'PyQt4']
filenames = [numpy_fn, scipy_fn, pyqt4_fn]
filenames_long = ['binary_dependencies\\'+fn for fn in filenames]
urls = ["https://dl.dropboxusercontent.com/u/78754747/binary_dependencies/"+fn for fn in filenames]

if not os.path.isdir('binary_dependencies'):
    os.mkdir('binary_dependencies')
for i in range(len(names)):
    try:
        exec("import {}".format(names[i]))
    except ImportError:
        if not os.path.isfile(filenames_long[i]):
            print("Downloading {}".format(names[i]))
            local_filename, headers = urlretrieve(urls[i])
            os.rename(local_filename,filenames_long[i])
            print("{} downloaded successfully".format(names[i]))
        pip.main(['install', filenames_long[i]])