# JPEG2000转化手册
本文档提供在 Ubuntu 20.04 LTS 下将 TIFF 转化为无损和有损 JPEG2000 格式的方法。

## 1. 安装前准备
### 1.1 安装exiftool

    sudo apt install exiftool 

### 1.2 安装Pillow

    pip install pillow

### 1.4 安装image_processing

    pip instll git+https://github.com/mengjinzhao/image-processing.git

默认的安装路径为 ~/.local/lib/python3.8/site-packages（取决于系统Python的版本）

### 1.5 安装Kakadu
kakadu是处理JPEG2000压缩程序的核心部分，来自于kakadusoftware.com。将kakadu文件夹拷贝至/opt/kakadu.

## 2. 转成JPEG2000

将image-processing代码库中的main-convert.py 拷贝出来。

    cp ~/.local/lib/python3.8/site-packages/main-convert.py ~/

main-convert.py中的内容如下：

    #!/Users/jinzhao/opt/anaconda3/bin/python3
    import os
    from image_processing.derivative_files_generator import DerivativeFilesGenerator

    derivatives_gen = DerivativeFilesGenerator(kakadu_base_path="/opt/kakadu")

    SOURCE_FOLDER = "/media/jinzhao/sda4/SOURCE"
    OUTPUT_FOLDER = "/media/jinzhao/sda4/OUTPUT"

    tif_files = os.listdir(SOURCE_FOLDER)
    tif_files.sort()
    for tif_file in tif_files:
            tif_path = os.path.join(SOURCE_FOLDER, tif_file)
            derivatives_gen.generate_derivatives_from_tiff(tif_path, OUTPUT_FOLDER)
        
其中，SOURCE_FOLDER为原图所在目录， OUTPUT_FOLDER为输出目录，每次转化时按需要更改目录。

开始转化：

    cd ~ && python3 main-convert.py

**注意**：TIFF所在外部磁盘的格式均为NTFS，挂载至Ubuntu Linux系统时需要安装paragon-ntfs以实现自动挂载。具体参见paragon-ntfs相关的文档。

## 3. 代码更新时如何处理
如果代码更改，开发人员mengjinzhao会将更新后的代码同步至 https://github.com/mengjinzhao/image-processing.git ，使用人员按照以下步骤更新：

    cd ~
    git clone https://github.com/mengjinzhao/impage-processing.git
    rsync -ave --delete ~/image-processing/image_processing/* ~/.local/lib/python3.8/site-packages/image_processing/
