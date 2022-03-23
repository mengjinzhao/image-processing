#!/bin/bash
#此脚本完成的功能是：在转换成JPEG2000的格式之前，将TIFF文件夹下的tif文件
#转移到同一文件夹下，并删除此前存储的JPG文件。

#BASE_DIR为源文件夹，其结构应该是：报纸种类/月份/TIFF/XXXX-19411021-01.tif
#DES_DIR为TIF转移后的存储文件夹，为后续转为JPEG2000文件做准备。

BASE_DIR=""
DES_DIR=""

for SUB_DIR in $(ls -1 $BASE_DIR)
do
    #将TIFF文件夹下的tif文件转移到目的文件夹，其中SUB_DIR为月份命名的文件夹
    mv $SUB_DIR/TIFF/*.tif $DES_DIR
    
    #删除TIFF文件夹
    rmdir $SUB_DIR/TIFF

    #删除以月份命名的文件夹下的JPG文件
    find $SUB_DIR/JPG -type f *.jpg -exec rm {} +

    #删除JPG文件夹
    rmdir $SUB_DIR/JPG
done

#删除名称中含有“封底”、“封面”、“空白”、“书脊”、“书签”的tif文件
find $DES_DIR -type f -name *封底*.tif -exec rm {} +
find $DES_DIR -type f -name *封面*.tif -exec rm {} +
find $DES_DIR -type f -name *空白*.tif -exec rm {} +
find $DES_DIR -type f -name *书脊*.tif -exec rm {} +
find $DES_DIR -type f -name *书签*.tif -exec rm {} +
find $DES_DIR -type f -name *书底*.tif -exec rm {} +
find $DES_DIR -type f -name *书面*.tif -exec rm {} +