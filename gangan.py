import glob
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def main():
    S = 64 # size of one picture
    n_img = 5*5

    print('Enter relative path to the directry that has pictures:')
    dir_name = str(input())
    files =glob.glob(dir_name + '/*')
    ims = []
    for i,file in enumerate(files):
        if i>=n_img:
            break
        print(file)
        im = Image.open(file)
        w, h = im.size
        w_mid, h_mid = int(w/2), int(h/2)
        unit = int(min(w, h)/2)
        im_crop = im.crop((w_mid-unit, h_mid-unit, w_mid+unit, h_mid+unit))
        im_resize =  im_crop.resize((S,S))
        ims.append(np.array(im_resize))

    ims = np.array(ims)
    ims = ims.reshape((5,5,S,S,3))
    ims = ims.transpose(0,2,1,3,4)
    ims = ims.reshape((5*S,5*S,3))

    plt.imsave('result.png', ims)

if __name__=='__main__':
    main()
