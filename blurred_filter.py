import cv2
import os
import numpy as np
import shutil

#### Getting filenames of images
filepath = '[insert filepath of source]'
all_imgs = os.listdir(filepath)
all_imgs.sort()
##print(all_imgs)

#### Filtering blurred images using laplacian
save_dir = '[insert filepath of destination]'
if os.path.isdir(save_dir):
    pass
else:
    os.mkdir(save_dir)

i,j=0,0
for n,image in enumerate(all_imgs):
    path = os.path.join(filepath,image)    
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    score = np.max(cv2.convertScaleAbs(cv2.Laplacian(gray, 3)))
    #### If image score > 200, move to filtered2
    #### Else, print File blurred and continue to next image
    print(f'File: {image}    Score: {score}')
    if score >= 200:
        save_path = os.path.join(save_dir,image)
        shutil.copy(path, save_path)
        print('File moved successfully')
        i+=1
    else:
        print(f'    File is a blurred')
        j+=1
        continue

print(f'There are {i} good imges \n There are {j} blurred images')
