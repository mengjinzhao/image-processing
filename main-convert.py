#!/Users/jinzhao/opt/anaconda3/bin/python3
import os
from image_processing.derivative_files_generator import DerivativeFilesGenerator

derivatives_gen = DerivativeFilesGenerator(kakadu_base_path="/Library/Kakadu/8.0.5/bin/")
SOURCE_FOLDER = "/Users/jinzhao/Work"
OUTPUT_FOLDER = "/Users/jinzhao/OUTPUT"

tif_files = os.listdir(SOURCE_FOLDER)
tif_files.sort()
for tif_file in tif_files:
        tif_path = os.path.join(SOURCE_FOLDER, tif_file)
        derivatives_gen.generate_derivatives_from_tiff(tif_path, OUTPUT_FOLDER)
