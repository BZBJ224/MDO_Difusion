from ase.io import write
from src.rotate import rotate
from src.decode import decode
from PIL import Image
from tqdm import tqdm
import numpy as np
import os

def rgb2gray(img):
    b=img[:,:,0].copy()
    g=img[:,:,1].copy()
    r=img[:,:,2].copy()

    out = r/3 + g/3 + b/3
    out = out.astype(np.uint8)

    return out

def fix_rotate(PATH_PNG):
    filename = os.listdir(PATH_PNG)
    PATH_FIX = '%s/TMP'%PATH_PNG
    os.makedirs(PATH_FIX, exist_ok=True)
    for i in filename:
        im = Image.open('%s/%s'%(PATH_PNG, i))
        im = rotate(im)
        img = Image.fromarray(im)
        img.save('%s/%s'%(PATH_FIX, i))

def main(PATH_CIF, PATH_PNG):
    fix_rotate(PATH_PNG)
    pad = np.array([0.5,0.5,0.5])
    filename = os.listdir('%s/TMP'%PATH_PNG)
    for i in tqdm(filename):
        img = rgb2gray(np.array(Image.open('%s/TMP/%s'%(PATH_PNG,filename)).convert('RGB')))
        try:
            atoms, energy = decode(np.array(img)/255, pad)
            dis = atoms.get_distance([atom.index for atom in atoms if atom.symbol == 'C'][0],
                               [atom.index for atom in atoms if atom.symbol == 'H'][0],mic=True)
            if dis <=1.15 :
                write('%s/%s_%s.cif'%(PATH_CIF, atoms.symbols, i),atoms)
        
        except Exception as e:
            pass

if __name__ == '__main__':
    PATH_CIF = '/path/to/cif'
    PATH_PNG = '/path/to/png'
    main(PATH_CIF, PATH_PNG)