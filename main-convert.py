#!/usr/bin/python3
import os
import magic
from osgeo import gdal
import subprocess
from image_processing.derivative_files_generator import DerivativeFilesGenerator

derivatives_gen = DerivativeFilesGenerator(kakadu_base_path="/Library/Kakadu/8.0.5/bin")

"""
 ！！！注意！！！每次使用时只改动以下 3 行即可。
 SOURCE_FOLDER：输入图片的路径
 TMP_FOLDER：临时存放转出的无损 TIFF 图片的路径
 OUTPUT_FOLDER：输出 JP2 格式图片的路径
"""

SOURCE_FOLDER = "/Users/jinzhao/Work"
TMP_FOLDER = "/Users/jinzhao/TMP"
OUTPUT_FOLDER = "/Users/jinzhao/OUTPUT"

GDAL_OPTIONS = '-co PROFILE=GeoTIFF -co COMPRESS=NONE'
GDAL_OPTIONS_BL = '-co PROFILE=BASELINE -co COMPRESS=NONE'
EXIFCMD = '/opt/homebrew/bin/exiftool'

tif_files = os.listdir(SOURCE_FOLDER)
tif_files.sort()
for tif_file in tif_files:
    tif_path = os.path.join(SOURCE_FOLDER, tif_file)
    tif_file_info = magic.from_file(tif_path)
    EXIF_INFO = subprocess.check_output([EXIFCMD,'-X',tif_path])
    EXIF_INFO = EXIF_INFO.decode('utf-8')
    tmp_tif_path = os.path.join(TMP_FOLDER, tif_file)

    if "compression=none" in tif_file_info:
        print(tif_path + " 未被压缩，即将处理该图片为JPEG2000格式。")
        if "AToB0" in EXIF_INFO:
            gdal.Translate(tmp_tif_path, tif_path, options = GDAL_OPTIONS_BL)
            derivatives_gen.generate_derivatives_from_tiff(tmp_tif_path, OUTPUT_FOLDER)
        else:
            derivatives_gen.generate_derivatives_from_tiff(tif_path, OUTPUT_FOLDER)
        print("转换 " + tif_path + " 为JPEG2000格式完毕。")
        print("**************************************")
    else:
        print(tif_path + " 使用了 LZW 压缩，即将处理该图片为无损 TIFF 格式。")
        if "AToB0" in EXIF_INFO:
            gdal.Translate(tmp_tif_path, tif_path, options = GDAL_OPTIONS_BL)
            print("已经将 " + tif_path + " 扩展为无压缩 TIFF，临时存放处为 " + tmp_tif_path + "并转换为 JPEG2000格式。")
            derivatives_gen.generate_derivatives_from_tiff(tmp_tif_path, OUTPUT_FOLDER)
        else:
            gdal.Translate(tmp_tif_path, tif_path, options = GDAL_OPTIONS)
            print("已经将 " + tif_path + " 扩展为无压缩 TIFF，临时存放处为 " + tmp_tif_path + "并转换为 JPEG2000格式。")
            derivatives_gen.generate_derivatives_from_tiff(tmp_tif_path, OUTPUT_FOLDER)
        
        print("转换 " + tmp_tif_path + " 为JPEG2000格式完毕。")
        print("**************************************")
