#!/bin/bash
#此脚本的功能是将转换后的jp2文件按照日期归纳
#每天一个文件夹
#每次使用修改BASE_DIR的路径，即转换后的JP2目的文件夹

BASE_DIR="/tmp/test-tiff"
cd $BASE_DIR

for SUB_DIR in $(ls -1 $BASE_DIR)
do
	cd $SUB_DIR
	for DAY_DIR in $(ls -1|awk -F "-" '{print $2}'|sort|uniq)
	do
		mkdir $DAY_DIR
		mv *-$DAY_DIR-*.tif $DAY_DIR
	done
	cd ..
done
