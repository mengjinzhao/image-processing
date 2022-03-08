#!/usr/bin/python3
import os
import magic
from osgeo import gdal

from image_processing.derivative_files_generator import DerivativeFilesGenerator

derivatives_gen = DerivativeFilesGenerator(kakadu_base_path="/opt/kakadu/")

SOURCE_FOLDER = "/Users/jinzhao/Work"
TMP_FOLDER = "/Users/jinzhao/TMP"
OUTPUT_FOLDER = "/Users/jinzhao/OUTPUT"

GDAL_OPTIONS = '-co PROFILE=BASELINE -co COMPRESS=NONE'

tif_files = os.listdir(SOURCE_FOLDER)
tif_files.sort()
for tif_file in tif_files:
    tif_path = os.path.join(SOURCE_FOLDER, tif_file)
    tif_file_info = magic.from_file(tif_path)
    if "compression=none" in tif_file_info:
        print(tif_path + " 未被压缩，即将处理该图片为JPEG2000格式。")
        derivatives_gen.generate_derivatives_from_tiff(tif_path, OUTPUT_FOLDER)
        print("转换 " + tif_path + " 为JPEG2000格式完毕。")
        print("**************************************")
    else:
        print(tif_path + " 使用了 LZW 压缩，即将处理该图片为无损 TIFF 格式。")
        tmp_tif_path = os.path.join(TMP_FOLDER, tif_file)
        gdal.Translate(tmp_tif_path, tif_path, options = GDAL_OPTIONS)
        print("已经将 " + tif_path + " 扩展为无压缩 TIFF，临时存放处为 " + tmp_tif_path + "并转换为 JPEG2000格式。")
        
        derivatives_gen.generate_derivatives_from_tiff(tmp_tif_path, OUTPUT_FOLDER)
        print("转换 " + tmp_tif_path + " 为JPEG2000格式完毕。")
        print("**************************************")
