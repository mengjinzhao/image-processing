import os
import magic
from osgeo import gdal

PATH = '/Users/jinzhao/Work'
OUTPATH = '/Users/jinzhao/OUTPUT'
GDAL_OPTIONS = '-co PROFILE=BASELINE -co COMPRESS=NONE'

TIFF_FILES = os.listdir(PATH)
TIFF_FILES.sort()

for TIFF_FILE in TIFF_FILES:
    TIFF_FILE_PATH = os.path.join(PATH, TIFF_FILE)
    TIFF_FILE_INFO = magic.from_file(TIFF_FILE_PATH)
    if "compression=none" in TIFF_FILE_INFO:
        print(TIFF_FILE + " 未被压缩。")
    else:
        NEW_TIFF_FILE_PATH = os.path.join(OUTPATH, TIFF_FILE)
        gdal.Translate(NEW_TIFF_FILE_PATH, TIFF_FILE_PATH, options = GDAL_OPTIONS)
        if "compression=none" in magic.from_file(NEW_TIFF_FILE_PATH):
            print(TIFF_FILE + " 解压缩成功！")
