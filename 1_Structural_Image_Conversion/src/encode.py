import numpy as np
from src.symbols import sym_list

def encode(atoms,pad):
    zero_pad = np.zeros([6,8])
    cov_c_l = np.ones([6,6])
    cell_length = atoms.get_cell_lengths_and_angles()

    cell_length_gaus = (np.random.multivariate_normal(cell_length,cov_c_l,(120),'raise')).T
    cell_length_gaus[:3,:] /= 30
    cell_length_gaus[3:,:] /= 150
    cell_length_gaus = np.concatenate([zero_pad,cell_length_gaus],axis=1)

    pos, pos_gaus = atoms.get_scaled_positions(), []
    pos_pad = (2/3*(pos-pad) + pad)*100
    cov_pos = np.ones([3,3])
    for i in pos_pad:
        x = np.random.multivariate_normal(i,cov_pos,(40),'raise')
        pos_gaus.append((x.T).reshape(-1))
    pos_gaus = np.array(pos_gaus)/100

    sym, sym_gaus = atoms.get_chemical_symbols(), []
    sym_index = np.array(sym_list(sym,' '))*10
    cov_sym = np.ones([len(sym_index),len(sym_index)])
    sym_gaus = (np.random.multivariate_normal(sym_index,cov_sym,(7),'raise')).T/ 400

    zero_pad = np.zeros([np.shape(pos_gaus)[0],1])
    sym_pos = np.concatenate([sym_gaus,zero_pad,pos_gaus],axis=1)

    zero_pad = np.zeros([1,128])
    total = np.concatenate([cell_length_gaus,zero_pad,sym_pos],axis=0)
    zero_pad = np.zeros([128-total.shape[0],128])

    total = np.concatenate([total,zero_pad],axis=0)
    # print(total.shape)

    return total

if __name__ == '__main__':
    pass
else:
    print('import encode')