'''
  Python Script for solving TryHackMe Advent of Cyber Day 16 Challenges
  @requirements: pyexiftool is required to run the script
                 place the downloaded zip file from TryHacKMe into a directory named zip in current directory
                 and then name the zip file as final.zip
'''
import os
import zipfile
import exiftool

# defining some constants
DOWNLOADED_ZIP_NAME = 'zip/final.zip'
MAIN_ZIP_EXTRACT_PATH = 'zip/extracted/'
SUB_ZIP_EXTRACT_PATH = 'zip/internal/'


# extracting the challenge zip
with zipfile.ZipFile(DOWNLOADED_ZIP_NAME) as zip_ref:
    zip_ref.extractall(MAIN_ZIP_EXTRACT_PATH)


# solving first flag
files = os.listdir(MAIN_ZIP_EXTRACT_PATH)
for f in files:
    with zipfile.ZipFile(MAIN_ZIP_EXTRACT_PATH + f) as zip_ref:
        zip_ref.extractall(SUB_ZIP_EXTRACT_PATH)
files = os.listdir(SUB_ZIP_EXTRACT_PATH)
print('#1 How many files did you extract(excluding all the .zip files)\nAnswer = {}'.format(len(files)))


# solving second flag
os.chdir(SUB_ZIP_EXTRACT_PATH)
with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(os.listdir())
count_version = 0
for m in metadata:
    if 'XMP:Version' in m and m['XMP:Version'] == 1.1:
        count_version += 1
print('#2 How many files contain Version: 1.1 in their metadata?\nAnswer = {}'.format(count_version))


# solving third flag
password_file = ''
for f in files:
    with open(f, encoding='utf8', errors='ignore') as fd:
        if 'password' in fd.read():
            password_file = f
print('#3 Which file contains the password?\nAnswer {}'.format(password_file))
