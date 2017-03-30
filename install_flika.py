from urllib.request import urlretrieve
import os, sys
import pip

version = sys.version_info
pyver = "{}{}".format(version.major, version.minor)
if version.major != 3 or version.minor not in [5, 6]:
	print("This install script requires Python 3.5 or 3.6. Your version of python is {}.{}. Flika install Failed.".format(version.major, version.minor))
	sys.exit()

numpy_fn  = "numpy-1.12.1+mkl-cp{0}-cp{0}m-win_amd64.whl".format(pyver)
scipy_fn  = "scipy-0.19.0-cp{0}-cp{0}m-win_amd64.whl".format(pyver)
skimage_fn = "scikit_image-0.13.0-cp{0}-cp{0}m-win_amd64.whl".format(pyver)
names = ['numpy', 'scipy', 'skimage']
filenames = [numpy_fn, scipy_fn, skimage_fn]
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

pip.main(['install', 'flika'])
