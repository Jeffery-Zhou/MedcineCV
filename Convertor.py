import openslide
import numpy as np
import scipy.misc
import imageio
import math
import PIL
import sys
import os

SCALE_FACTOR = 32 
# put this file under the path of the folder containing .svs file. 
def fileProcessor(filepath, output_path):
    slide = openslide.open_slide(filepath)
    large_w, large_h = slide.dimensions
    new_w = math.floor(large_w / SCALE_FACTOR)
    new_h = math.floor(large_h / SCALE_FACTOR)
    level = slide.get_best_level_for_downsample(SCALE_FACTOR)
    whole_slide_image = slide.read_region((0, 0), level, slide.level_dimensions[level])
    whole_slide_image = whole_slide_image.convert("RGB")
    img = whole_slide_image.resize((new_w, new_h), PIL.Image.BILINEAR)
    imageio.imwrite(output_path, img)


ROOT_PATH = "/Volumes/MedImage"
OUTPUT_PATH = "./images"

files= os.listdir(ROOT_PATH) 

file_path_lst = []
output_path_lst = []
for file in files:
     if not os.path.isdir(file): 
         if "svs" in file:
            file_path = ROOT_PATH + "/" + file
            file_path_lst.append(file_path)
            output_path = OUTPUT_PATH + "/" + file[:-4] + '.png'
            output_path_lst.append(output_path)
            
# for i in range(10):
#     print(file_path_lst[i])
#     print(output_path_lst[i])           
for i in range(100, 200):
    try:
        fileProcessor(file_path_lst[i], output_path_lst[i])
    except IOError:
        print(i, "has Error, and the path: ", file_path_lst[i])
    else:
        print(i, "Finished")
    
    # Issue index: 48  '/Volumes/MedImage/TCGA-GM-A3XL-01Z-00-DX1.CCE8AA1D-9194-4E49-9546-DBF25A35847C.svs'
    # 
    

