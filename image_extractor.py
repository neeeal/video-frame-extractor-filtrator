import os
import shutil
import cv2


#### Accessing files through filepath
filepath = '[insert filepath of source]'
class_names = ['objects']

#### Extracting frames from videos
save_dir = '[insert filepath of destination]'
if os.path.isdir(save_dir):
    pass
else:
    os.mkdir(save_dir)
 
for m,c in enumerate(class_names[:]):
    path = filepath#os.path.join(filepath,c)
    for n,img in enumerate(os.listdir(path)):
        print(f'Currently processing class {m}    file #{n}')
        # Opens the Video file
        cap= cv2.VideoCapture(os.path.join(path,img))
        i=0
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == False:
                break
            cv2.imwrite(f'{save_dir}/{c}_{img.split(".")[0]}_frame_{i}.jpg',frame)
            #cv2.imwrite(save_dir+img+c+str(i)+'.jpg',frame)
            i+=1
    cap.release()
    cv2.destroyAllWindows()

print(f'There are {len(os.listdir(save_dir))} images')
