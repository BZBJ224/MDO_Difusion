from ase.io import read,write
import numpy as np 



def rotate(atoms,*args):		
	'''
	example: rotate(atoms,'xy','xz','yz')
	return [atoms,rotate_xy,rotate_xz,rotate_yz]
	'''
	data = [atoms]
	cell = atoms.get_cell_lengths_and_angles()
	pos = atoms.positions
	a,b,c = [cell[0],cell[3]],[cell[1],cell[4]],[cell[2],cell[5]]
	x,y,z = pos[:,0].copy(), pos[:,1].copy(), pos[:,2].copy()
	for i in args:
		if i == 'xy':
			cell = [b[0],a[0],c[0],b[1],a[1],c[1]]
			pos = np.concatenate([y,x,z]).reshape([-1,3])
		if i == 'xz':
			cell = [c[0],b[0],a[0],c[1],b[1],a[1]]
			pos = np.concatenate([z,y,x]).reshape([-1,3])
		if i == 'yz':
			cell = [a[0],c[0],b[0],a[1],c[1],b[1]]
			pos = np.concatenate([x,z,y]).reshape([-1,3])
		new_atoms = atoms.copy()
		new_atoms.cell = cell
		new_atoms.positions = pos 
		data.append(new_atoms)

	return data

def trans(atoms):
	a, data = atoms, []
	base = np.array([0.18,0.18,0.05])
	for i in range(6):
		for j in range(6):
			for k in range(6):
				atoms = a.copy()
				new_pos = a.get_scaled_positions() + base*np.array([i,j,k])
				atoms.set_scaled_positions(new_pos)
				data.append(atoms)
	return data

