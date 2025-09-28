
def sym_list(sym, index):
    sym_index = {'Zn':30,'Cr':24,'O':8,'H':2,'C':5,'Al':13,'Zn':28,'Ga':31,'Zr':40,'In':49}
    index_sym = {'30':'Zn','31':'Zn','29':'Zn', '23':'Cr', '24':'Cr', '25':'Cr',
                    '9':'O','8':'O','7':'O', '3':'H','2':'H','1':'H',
                    '4':'C','5':'C','6':'C', '12':'Al','13':'Al','14':'Al',
                    '27':'Zn','28':'Zn','29':'Zn', '30':'Ga','31':'Ga','33':'Ga',
                    '39':'Zr','40':'Zr','41':'Zr', '48':'In','49':'In','50':'In'}
    try:
        index = [sym_index[i] for i in sym]
        return index
    except:
        symbols = ''
        for i in index:
            symbols += index_sym['%d'%i]
        # print(symbols)
        return symbols

if __name__ == '__main__':
    pass
else:
    print('import symbols')