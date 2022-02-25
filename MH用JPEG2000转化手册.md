# JPEG2000转化手册
本文档提供在 Ubuntu 20.04 LTS 下将 TIFF 转化为无损和有损 JPEG2000 格式的方法。

## 1. 安装前准备
### 1.1 安装exiftool

    sudo apt install exiftool 

### 1.2 安装Pillow

    pip install pillow

### 1.3 安装image_processing

    pip install git+https://github.com/mengjinzhao/image-processing.git

默认的安装路径为 ~/.local/lib/python3.8/site-packages/image_processing（取决于系统Python的版本）

### 1.4 安装Kakadu
kakadu是处理JPEG2000压缩程序的核心部分，来自于kakadusoftware.com。
将kakadu文件夹拷贝至/opt/kakadu，并将该目录下的libkdu_v80R.so拷贝至/usr/lib：

    sudo cp /opt/kakadu/libkdu_v80R.so /usr/lib/

或者：

    sudo ln -s /opt/kakadu/libkdu_v80R.so /usr/lib/

## 2. 转成JPEG2000

将 image-processing 代码克隆至用户主目录：

    cd ~ && git clone https://github.com/mengjinzhao/image-processing.git

拷贝入口程序 main-convert.py 至主目录：

    cp ~/image-processing/main-convert.py ~/

使用文本编辑器或者 PyCharm 打开 ~/main-convert.py，找到如下两行：

    SOURCE_FOLDER = "/media/jinzhao/sda4/SOURCE"
    OUTPUT_FOLDER = "/media/jinzhao/sda4/OUTPUT"

其中，SOURCE_FOLDER 为原图所在路径， OUTPUT_FOLDER 为输出路径，每次转化时按需要更改目录，在 PyCharm 中修改后可以直接运行，或者直接在命令行下运行：

    python3 ~/main-convert.py

**注意**：TIFF 所在外部磁盘的格式均为 NTFS，挂载至 Ubuntu Linux 系统时需要安装 paragon-ntfs 以实现自动挂载。具体请参见paragon-ntfs相关的文档。

## 3. 代码更新后的处理方法
如果代码更改，主要是 image_process 下的 Python 文件有更改，开发人员mengjinzhao会将更新后的代码同步至 https://github.com/mengjinzhao/image-processing.git ，使用人员按照以下步骤更新：

    cd ~/image-processing
    git pull
    rsync -ave --delete ~/image-processing/image_processing/* ~/.local/lib/python3.8/site-packages/image_processing/
