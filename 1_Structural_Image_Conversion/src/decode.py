import numpy as np
from src.symbols import sym_list
from ase import Atoms

def decode(image,pad):
    image = remove_zero_pad(image)
    cell_length = np.mean(image[:6,8:],axis=1)
    cell_length[:3] *= 30
    cell_length[3:] *= 150
    sym_pos = image[6:,:]
    symbols = np.mean(sym_pos[:,:7], axis=1)
    # print(np.round(symbols*40))
    sym = sym_list('_',np.round(symbols*40))
    pos = sym_pos[:,8:].reshape(symbols.shape[0],3,40)
    positions = (np.mean(pos,axis=2)-pad)*3/2 + pad

    atoms = Atoms(sym,
        cell = cell_length,
        positions = positions,
        pbc = True)
    atoms.set_scaled_positions(positions)

    energy = 0
    # energy = np.mean(image[-2:,:].reshape(-1),axis=0)

    return atoms, energy

def remove_zero_pad(image):
    total = np.sum(image,axis=1)
    return image[np.where(total > 10)]

if __name__ == '__main__':
    pass
else:
    print('import decode')