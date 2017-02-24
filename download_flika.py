from urllib.request import urlretrieve
import zipfile
import os, sys

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