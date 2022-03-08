本文提供了安装GDAL的方法：
## 1. 安装前准备
### 1.1 安装Magic
Magic 的作用是在 Python 中获取文件的相关信息，其作用类似 Linux 下 file 命令，在 Ubuntu 和 macOS 下安装时略有不同。
在 Ubuntu 20.04 LTS 下：

    pip install python-magic

在 macOS Monterey 下：

    pip install python-magic-bin==0.4.14

### 1.2 安装GDAL
在 Ubuntu 20.04 LTS 下:

    sudo apt install gdal-bin
    sudo apt install libgdal-dev
    export CPLUS_INCLUDE_PATH=/usr/include/gdal
    export C_INCLUDE_PATH=/usr/include/gdal
    pip install GDAL

## 2. 使用GDAL
本部分主要使用 gdal_translate 将 LZW 算法压缩过的TIFF图片转化为未压缩的版本。
### 2.1 使用 Linux 命令行
使用 Linux 命令行进行转化的方式如下：

    gdal_translate input.tif output.tif -co PROFILE=BASELINE -co COMPRESS=NONE

此处增加 <em>-co PROFILE=BASELINE</em> 的原因是后续 JPEG2000 的支持有限，所以先转化成 **BASELINE**，否则 Kakadu 会报错或发出警告。
### 2.2 在 Python 中调用 API：
在 Python 中调用的方式略有不同，主要是输出文件在前，输入文件在后：

    gdal.Translate('output.tif', 'input.tif', options = '-co PROFILE=BASELINE -co COMPRESS=NONE')

