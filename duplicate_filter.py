import imagehash
from PIL import Image
import numpy as np
import os
import shutil
def alpharemover(image):
    if image.mode != 'RGBA':
        return image
    canvas = Image.new('RGBA', image.size, (255,255,255,255))
    canvas.paste(image, mask=image)
    return canvas.convert('RGB')
def with_ztransform_preprocess(hashfunc, hash_size=8):
    def function(path):
        image = alpharemover(Image.open(path))
        image = image.convert("L").resize((hash_size, hash_size), Image.ANTIALIAS)
        data = image.getdata()
        quantiles = np.arange(100)
        quantiles_values = np.percentile(data, quantiles)
        zdata = (np.interp(data, quantiles_values, quantiles) / 100 * 255).astype(np.uint8)
        image.putdata(zdata)
        return hashfunc(image)
    return function
dhash_z_transformed = with_ztransform_preprocess(imagehash.dhash, hash_size = 8)
#### Getting filenames of images
filepath = '[insert filepath of source]'
all_imgs = os.listdir(filepath)
all_imgs.sort()
#### Filtering duplicate images using hash
save_dir = '[insert filepath of destination]'
if os.path.isdir(save_dir): pass
else: os.mkdir(save_dir)
img_ls=[]
i,j=0,0
for n,img in enumerate(all_imgs):
    print(f'Currently doing {n}')
    path = f'{filepath}/{img}'
    if n==0:
        img_ls.append(dhash_z_transformed(path))
        continue
    temp = dhash_z_transformed(path)
    #### If image is not a duplicate, move it to filtered1 folder
    #### Else, print File is a duplicate and continue to next image
    if temp not in img_ls:
        save_path = os.path.join(save_dir,img)
        shutil.copy(path, save_path)
        print('File moved successfully')
        i+=1
    else:
        print(f'File {img} is a duplicate')
        j+=1
        continue
    img_ls.append(temp)
print(f'There are {i} good imges \n There are {j} dup images')
