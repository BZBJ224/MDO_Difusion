from ase.io import read
import numpy as np
from PIL import Image
from src.encode import encode
from src.decode import decode
import os, warnings
from tqdm import tqdm

warnings.filterwarnings("ignore")

def main(PATH_CIF, PATH_PNG):

    file_name = os.listdir(PATH_CIF)
    distance = []
    for i in tqdm(file_name,ncols=100):
        a = read('%s/%s'%(PATH_CIF,i))
        pad = np.array([0.5,0.5,0.5])
        img_atoms = encode(a,pad)
        im = Image.fromarray(img_atoms*255)
        im = im.convert('RGB')
        im.save('%s/%s.png'%(PATH_PNG,i))

if __name__ =='__main__':
    PATH_CIF = '/path/to/cif'
    PATH_PNG = '/path/to/png'
    main(PATH_CIF, PATH_PNG)
