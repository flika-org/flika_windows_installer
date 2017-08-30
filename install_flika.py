from urllib.request import urlretrieve
import os, sys
import pip

version = sys.version_info
pyver = "{}{}".format(version.major, version.minor)
if version.major != 3 or version.minor not in [5, 6]:
	print("This install script requires Python 3.5 or 3.6. Your version of python is {}.{}. Flika install Failed.".format(version.major, version.minor))
	sys.exit()

class Package(object):
    def __init__(self, name):
        self.name = name
    def set_url(self, url, filename):
        self.url = url
        self.filename = filename
        self.filename_long = 'binary_dependencies\\' + filename


numpy__ = Package('numpy')
scipy__ = Package('scipy')
scikit_image__ = Package('skimage')
scikit_learn__ = Package('sklearn')
if version.minor == 5:
    numpy__.set_url("https://www.dropbox.com/s/c2xx6267uxv7rcq/numpy-1.13.1%2Bmkl-cp35-cp35m-win_amd64.whl?dl=1", "numpy-1.13.1+mkl-cp35-cp35m-win_amd64.whl")
    scipy__.set_url("https://www.dropbox.com/s/eutra43dqvtbip1/scipy-0.19.1-cp35-cp35m-win_amd64.whl?dl=1", "scipy-0.19.1-cp35-cp35m-win_amd64.whl")
    scikit_image__.set_url("https://www.dropbox.com/s/qtw2pohf1facfaa/scikit_image-0.13.0-cp35-cp35m-win_amd64.whl?dl=1", "scikit_image-0.13.0-cp35-cp35m-win_amd64.whl")
    scikit_learn__.set_url("https://www.dropbox.com/s/jy5r6xi3421v4pt/scikit_learn-0.19.0-cp35-cp35m-win_amd64.whl?dl=1", "scikit_learn-0.19.0-cp35-cp35m-win_amd64.whl")
elif version.minor == 6:
    numpy__.set_url("https://www.dropbox.com/s/i8zpsl6x9dq3qd5/numpy-1.13.1%2Bmkl-cp36-cp36m-win_amd64.whl?dl=1", "numpy-1.13.1+mkl-cp36-cp36m-win_amd64.whl")
    scipy__.set_url("https://www.dropbox.com/s/ir6keud3tlxkgjm/scipy-0.19.1-cp36-cp36m-win_amd64.whl?dl=1", "scipy-0.19.1-cp36-cp36m-win_amd64.whl")
    scikit_image__.set_url("https://www.dropbox.com/s/it8udjxuv8x3ey8/scikit_image-0.13.0-cp36-cp36m-win_amd64.whl?dl=1", "scikit_image-0.13.0-cp36-cp36m-win_amd64.whl")
    scikit_learn__.set_url("https://www.dropbox.com/s/ig1h5flezv33tm9/scikit_learn-0.19.0-cp36-cp36m-win_amd64.whl?dl=1", "scikit_learn-0.19.0-cp36-cp36m-win_amd64.whl")

if not os.path.isdir('binary_dependencies'):
    os.mkdir('binary_dependencies')
for package in [numpy__, scipy__, scikit_image__, scikit_learn__]:
    try:
        exec("import {}".format(package.name))
    except ImportError:
        if not os.path.isfile(package.filename_long):
            print("Downloading {}".format(package.name))
            local_filename, headers = urlretrieve(package.url)
            os.rename(local_filename, package.filename_long)
            print("{} downloaded successfully".format(package.name))
        pip.main(['install', package.filename_long])
        
pip.main(['install', 'flika'])

