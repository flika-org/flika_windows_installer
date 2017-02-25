from urllib.request import urlretrieve
import zipfile
import os, sys

numpy_url = "https://drive.google.com/open?id=0B1nx_G74rPH5R0hfSzNRU3Q0NG8"
pyqt4_url = "https://drive.google.com/open?id=0B1nx_G74rPH5dTdVMk5zQVIzMms"
scipy_url = "https://drive.google.com/open?id=0B1nx_G74rPH5T09pWGZZakZEams"
urls = [numpy_url, pyqt4_url, scipy_url]
for url in urls:
	
if os.path.isdir('flika'):
	print('Flika directory already exists. No need to Download Flika.')
	sys.exit()
print("Downloading Flika...")
local_filename, headers = urlretrieve('http://github.com/flika-org/flika/archive/master.zip')
print("Successfully downloaded Flika. Extracting...")
with zipfile.ZipFile(local_filename, "r") as zf:
    zf.extractall()
print("Successfully Extracted Flika.")
os.rename('flika-master','flika')